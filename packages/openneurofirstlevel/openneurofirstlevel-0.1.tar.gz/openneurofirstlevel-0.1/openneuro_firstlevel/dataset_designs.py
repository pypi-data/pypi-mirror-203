"""Some datasets require customized reformatting of the events file to be compatible with the
rest of the code - this module houses those functions."""

import pdb

from nilearn.glm.first_level.design_matrix import make_first_level_design_matrix

from .utils import _get_frame_times, _add_parametric_modulation



def make_ds001734_design(img, events, confounds,
                         slice_time_ref, t_r, min_onset,
                         hrf_model, drift_model, high_pass,
                         rt_column):
    frame_times = _get_frame_times(img, confounds, t_r, slice_time_ref)
    regressors = _add_parametric_modulation(confounds, rt_column, events, frame_times,
                                            hrf_model, drift_model, high_pass, min_onset)
    add_cols = ['gain', 'loss']
    for col in add_cols:
        col_label = f'{col}_centered'
        events[col_label] = events[col] - events[col].mean()
        regressors = _add_parametric_modulation(regressors, col_label, events, frame_times,
                                                hrf_model, drift_model, high_pass, min_onset)

    design_matrix = make_first_level_design_matrix(
        frame_times,
        events=events[['onset', 'duration']],
        hrf_model=hrf_model,
        drift_model=drift_model,
        high_pass=high_pass,
        min_onset=min_onset,
        add_regs=regressors)
    design_matrix = design_matrix.drop(columns=['dummy'])
    return design_matrix
