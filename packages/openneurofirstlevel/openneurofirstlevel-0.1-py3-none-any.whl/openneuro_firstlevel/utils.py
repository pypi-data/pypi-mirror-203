import json
import os
import pdb

import numpy as np
from nilearn.interfaces.bids import get_bids_files
from nilearn.image import get_data
from nilearn.glm.first_level.design_matrix import make_first_level_design_matrix
from nilearn._utils.niimg_conversions import check_niimg
from nilearn.maskers import NiftiMasker



def get_tr_slice_time_ref(data_dir, derivatives_dir, task_label, img_filters=None):
    # Get slice_time_ref and the TR from the fMRIprep metadata
    # If slice timing correction was not done, slice_time_ref = 0 (frame times will not be shifted)
    # If slice timing correction was done, slice_time_ref determined from fMRI-prep outputs:
    # frame times will be shifted by +slice_time_ref * TR (usually +TR/2)
    # The filters are included to match the filters used internally by nilearn when 
    # querying the fMRIprep metadata.
    derivatives_path = os.path.join(data_dir, derivatives_dir)
    filters = [('task', task_label)]
    if img_filters is not None:
        for img_filter in img_filters:
            if img_filter[0] in ['acq', 'rec', 'run']:
                filters.append(img_filter)
    img_specs = get_bids_files(derivatives_path, modality_folder='func',
                               file_tag='bold', file_type='json',
                               filters=filters)
    specs = json.load(open(img_specs[0], 'r'))
    t_r = specs['RepetitionTime']
    if specs['SliceTimingCorrected'] == False:
        slice_time_ref = 0.0
    else:
        slice_time_ref = specs['SliceTimingRef']
    return t_r, slice_time_ref

def filter_subjects(subjects, imgs, events, exclude_subjects=None, include_subjects=None):
    assert exclude_subjects == None or include_subjects == None, \
        'Either exclude_subjects or include_subjects must be set to None!'
    if include_subjects is not None:
        keep_idx = np.nonzero(np.isin(subjects, include_subjects))[0]
    elif exclude_subjects is not None:
        keep_idx = np.nonzero(~np.isin(subjects, exclude_subjects))[0]
    else:
        keep_idx = np.arange(len(subjects))
    keep_subjects = [sub for i, sub in enumerate(subjects) if i in keep_idx]
    keep_imgs = [img for i, img in enumerate(imgs) if i in keep_idx]
    keep_events = [event for i, event in enumerate(events) if i in keep_idx]
    print(f'Excluding N={len(subjects) - len(keep_subjects)} subjects')
    return keep_subjects, keep_imgs, keep_events

def _get_frame_times(img, confounds, t_r, slice_time_ref):
    img = check_niimg(img, ensure_ndim=4)
    n_scans = get_data(img).shape[3]
    confounds_matrix = confounds.values
    assert confounds_matrix.shape[0] == n_scans, "Confounds rows doesn't match n_scans!"
    start_time = slice_time_ref * t_r
    end_time = (n_scans - 1 + slice_time_ref) * t_r
    frame_times = np.linspace(start_time, end_time, n_scans)
    return frame_times

def _add_parametric_modulation(regressors, column, events, frame_times, hrf_model, drift_model,
                               high_pass, min_onset):
    # Use the events variable "column" to create a parametric modulation regressor
    events_pm = events[['onset', 'duration', column]].copy()
    events_pm = events_pm.rename(columns={column: 'modulation'})
    design_pm = make_first_level_design_matrix(frame_times,
                                               events=events_pm,
                                               hrf_model=hrf_model,
                                               drift_model=drift_model,
                                               high_pass=high_pass,
                                               min_onset=min_onset)
    regressors[f'{column}_mod'] = design_pm['dummy'].values
    return regressors

def combine_run_masks(masks):
    # Combine masks from multiple runs by taking the product (logical and) of each run mask
    return NiftiMasker(np.prod(np.stack([nilearn.image.get_data(i) for i in masks]), axis=0))
