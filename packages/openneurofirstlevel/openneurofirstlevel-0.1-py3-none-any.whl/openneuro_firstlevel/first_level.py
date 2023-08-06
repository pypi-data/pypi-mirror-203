import pdb
import os
import json
import glob

import numpy as np
import pandas as pd
from nilearn.glm.first_level import first_level_from_bids, FirstLevelModel
from nilearn.plotting import plot_design_matrix, plot_stat_map, plot_contrast_matrix, plot_glass_brain
from nilearn.interfaces.fmriprep import load_confounds
from nilearn.interfaces.bids import get_bids_files
from nilearn._utils.niimg_conversions import check_niimg
from nilearn.image import get_data, concat_imgs, mean_img
from nilearn.glm.first_level.design_matrix import make_first_level_design_matrix
from nilearn.glm.contrasts import compute_fixed_effects
import matplotlib.pyplot as plt

from .utils import (filter_subjects, get_tr_slice_time_ref, _get_frame_times, 
                    _add_parametric_modulation, combine_run_masks)
from .diagnostics import est_all_contrast_vif



def get_contrasts(design_matrix, contrast_conditions):
    contrast_matrix = np.eye(design_matrix.shape[1])
    single_contrasts = dict([(column, contrast_matrix[i])
                            for i, column in enumerate(design_matrix.columns)])
    contrasts = [single_contrasts[cc[0]] - single_contrasts[cc[1]]
                 for cc in contrast_conditions]
    return contrasts

def make_design_matrix(img, events, confounds,
                       slice_time_ref, t_r, min_onset,
                       hrf_model, drift_model, high_pass,
                       rt_column):
    # Wrapper around nilearn make_first_level_design_matrix
    # that creates a design matrix with response time (RT) as a parametric
    # modulator in addition to the original unmodulated event regressors.
    # For the RT regressor, the amplitude (but not duration) of 
    # each event is scaled by the RT (cite Jeanette's paper), and the regressor
    # is not centered (demeaned). 
    frame_times = _get_frame_times(img, confounds, t_r, slice_time_ref)
    confounds = _add_parametric_modulation(confounds, rt_column, events, frame_times,
                                           hrf_model, drift_model, high_pass, min_onset)
    # Create full design matrix with original unmodulated regressor
    # and RT-modulated regressor
    design_matrix = make_first_level_design_matrix(
        frame_times,
        events=events[['onset', 'duration', 'trial_type']],
        hrf_model=hrf_model,
        drift_model=drift_model,
        high_pass=high_pass,
        min_onset=min_onset,
        add_regs=confounds)
    return design_matrix

def fit_single_subject(subject_id, imgs, events, data_dir, derivatives_dir, 
                       task_label, save_dir, min_onset=-24,
                       standardize=False, signal_scaling=0, **kwargs):
    n_runs = len(imgs)
    run_models, run_designs, run_masks = [], [], []
    space_label = kwargs['space_label']
    for run_ind in range(n_runs):
        run_imgs, run_events = imgs[run_ind], events[run_ind]
        if n_runs == 1:
            mask_fn = f'sub-{subject_id}_task-{task_label}_space-{space_label}*mask.nii.gz'
        else:
            mask_fn = f'sub-{subject_id}_task-{task_label}_run-{run_ind+1}_space-{space_label}*mask.nii.gz'
        mask_img = glob.glob(os.path.join(
            data_dir, derivatives_dir, f'sub-{subject_id}', 'func', mask_fn))[0]
        run_masks.append(mask_img)

        model = FirstLevelModel(t_r=kwargs['t_r'],
                                slice_time_ref=kwargs['slice_time_ref'],
                                hrf_model=kwargs['hrf_model'], 
                                drift_model=kwargs['drift_model'],
                                high_pass=kwargs['high_pass'], 
                                mask_img=mask_img,
                                smoothing_fwhm=kwargs['smoothing_fwhm'],
                                noise_model=kwargs['noise_model'],
                                min_onset=min_onset,
                                standardize=standardize, 
                                signal_scaling=signal_scaling,
                                subject_label=subject_id,
                                minimize_memory=False)

        # These parameters extract 6 basic head motion confounds + derivatives
        # and the average WM and CSF signal as confounds.
        # All confounds are demeaned. No scrubbing is done to remove
        # high motion volumes. 
        confounds, sample_mask = load_confounds(run_imgs,
                                                strategy=('motion', 'wm_csf'),
                                                motion='derivatives', wm_csf='basic',
                                                demean=True)
        run_events['duration'] = np.ones(len(run_events))  # Fix duration to 1s for all events
        design_matrix_fn = (make_design_matrix if kwargs['design_function'] is None 
                            else kwargs['design_function'])
        design_matrix = design_matrix_fn(run_imgs, run_events, confounds,
                                         kwargs['slice_time_ref'], 
                                         kwargs['t_r'], min_onset,
                                         kwargs['hrf_model'], 
                                         kwargs['drift_model'], 
                                         kwargs['high_pass'], 
                                         kwargs['rt_column'])
        design_mat_fig = plot_design_matrix(design_matrix)
        save_fn_base = f'task-{task_label}_run-{run_ind+1}'
        plt.savefig(os.path.join(save_dir, f'{save_fn_base}_design_matrix.png'))
        design_matrix.to_csv(os.path.join(save_dir, f'{save_fn_base}_design_matrix.csv'), 
                             index_label=False)
        model.fit(run_imgs, design_matrices=design_matrix)
        run_models.append(model)
        run_designs.append(design_matrix)
        # Save residuals
        res_path = os.path.join(save_dir, f'{save_fn_base}_residuals.nii.gz')
        res = model.residuals[0]
        res.header.set_data_dtype(np.float32)
        res.to_filename(res_path)
    return run_models, run_designs, run_masks

def analyze_contrasts(run_models, imgs, run_designs, run_masks, contrast_labels, 
                      task_label, contrast_conditions, subject_id, z_thresh, save_dir):
        contrasts = get_contrasts(run_designs[0], contrast_conditions)
        n_runs = len(run_models)
        # Not ideal to have two double for-loops, refactor
        for run_ind in range(n_runs):
            run_model, run_design, run_imgs = run_models[run_ind], run_designs[run_ind], imgs[run_ind]
            est_all_contrast_vif(run_design, contrasts, contrast_labels, task_label, save_dir, run_ind)

        for con_label, con in zip(contrast_labels, contrasts):
            all_run_stats = []
            for run_ind in range(n_runs):
                save_label = f'task-{task_label}_run-{run_ind+1}_contrast-{con_label}'
                run_model, run_design, run_imgs = run_models[run_ind], run_designs[run_ind], imgs[run_ind]
                run_stats = run_model.compute_contrast(con, output_type='all')
                all_run_stats.append(run_stats)
                run_stats['z_score'].to_filename(os.path.join(save_dir, f'{save_label}_z_scores.nii.gz'))
                z_fig = plt.figure(figsize=(12, 3))
                bg_img = mean_img(concat_imgs(run_imgs))
                plot_stat_map(run_stats['z_score'], threshold=z_thresh, bg_img=bg_img,
                              display_mode='z', cut_coords=(-25, 0, 50), black_bg=True,
                              figure=z_fig, title=f'{save_label}')
                plt.savefig(os.path.join(save_dir, f'{save_label}_zstatmap.png'))
                #plot_glass_brain(z_map, colorbar=True, threshold=norm.isf(0.001),
                #                 title=f'Nilearn Z map of {label} (unc p<0.001)',
                #                 plot_abs=False, display_mode='ortho')
                #plt.savefig(os.path.join(save_dir, f'sub{subject_id}_{label}_glass_brain.png'))
                #plot_contrast_matrix(con, design_matrix=design_matrix)
                #plt.savefig(os.path.join(save_dir, f'task-{task_label}_contrast-{con_label}_contrast_matrix.png'))
                plt.close('all')

            if n_runs > 1:
                # Compute precision-weighted run average fixed effect
                combined_mask = combine_run_masks(run_masks)
                combined_bg_img = mean_img(concat_imgs(imgs))
                combine_runs(all_run_stats, save_dir, task_label, con_label, z_thresh, 
                             combined_mask, combined_bg_img)

def combine_runs(run_stats, save_dir, task_label, contrast_label, z_thresh, mask, bg_img):
    save_label = f'task-{task_label}_run_avg_contrast-{contrast_label}'
    contrast_imgs = [stats['effect_size'] for stats in run_stats]
    variance_imgs = [stats['effect_variance'] for stats in run_stats]
    fixed_fx_contrast, fixed_fx_variance, fixed_fx_stat = compute_fixed_effects(
        contrast_imgs, variance_imgs, mask, precision_weighted=False)
    fixed_fx_stat.to_filename(os.path.join(save_dir, f'{save_label}_t_scores.nii.gz'))
    plot_stat_map(
        fixed_fx_stat, bg_img=bg_img, threshold=z_thresh, cut_coords=(-25, 0, 50),
        display_mode='z', black_bg=True, title=f'{save_label}')
    plt.savefig(os.path.join(save_dir, f'{save_label}_tstatmap.png'))

def run_first_level_analysis(data_dir, derivatives_dir, save_dir, **kwargs):
    for task_label in kwargs['task_labels']:
        if kwargs['t_r'] is None and kwargs['slice_time_ref'] is None:
            t_r, slice_time_ref = get_tr_slice_time_ref(data_dir, derivatives_dir, 
                                                        task_label,
                                                        img_filters=kwargs['img_filters'])
            kwargs['t_r'] = t_r
            kwargs['slice_time_ref'] = slice_time_ref
        # We use first_level_from_bids to get the image and event files,
        # but the model will be redefined with the appropriate mask image below
        # (subject-specific masks can't be passed to first_level_from_bids directly)
        throwaway_models, models_run_imgs, models_events, _ = \
            first_level_from_bids(data_dir, task_label, space_label=kwargs['space_label'],
                                  slice_time_ref=kwargs['slice_time_ref'],
                                  derivatives_folder=derivatives_dir,
                                  img_filters=kwargs['img_filters'])
        subject_labels = [m.subject_label for m in throwaway_models]
        all_subjects, all_imgs, all_events = filter_subjects(
            subject_labels, models_run_imgs, models_events,
            exclude_subjects=kwargs.get('exclude_subjects', None),
            include_subjects=kwargs.get('include_subjects', None))
        # Save list of included subjects
        subject_series = pd.Series(all_subjects)
        subject_series.to_csv(os.path.join(save_dir, f'included_subjects.csv'), 
                              index_label=False)

        # Fit model to each subject
        for sub, imgs, events in zip(all_subjects, all_imgs, all_events):
            subject_save_dir = os.path.join(save_dir, f'sub-{sub}')
            os.makedirs(subject_save_dir, exist_ok=True)
            run_models, run_designs, run_masks = fit_single_subject(
                sub, imgs, events, data_dir, derivatives_dir,
                task_label, subject_save_dir, **kwargs)
            analyze_contrasts(run_models, imgs, run_designs, 
                              run_masks, kwargs['contrast_labels'], task_label,
                              kwargs['contrast_conditions'], sub, 
                              kwargs['z_thresh'], subject_save_dir)
            plt.close('all')
