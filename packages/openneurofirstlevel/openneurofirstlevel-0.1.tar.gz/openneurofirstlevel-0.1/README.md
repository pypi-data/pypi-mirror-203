# openneurofirstlevel
This repo contains code for running first-level GLMs on OpenNeuro datasets. Much of the code has been repurposed from the nilearn package. The variance inflation factor code was adapted from code written by Jeanette Mumford. 

## Analysis Notes
HRF model: SPM (difference of two gamma functions) <br>
Drift model: DCT basis set, high-pass filter cutoff = 0.1Hz <br>
Noise model: AR(1) <br>
Spatial smoothing: None <br>
Confound regressors: head motion/translation + derivatives, average power in WM mask and CSF mask (14 confounds total). All are demeaned. <br>
Additionally, response times (RTs) are included as a parametric modulator confound regressor as described in Mumford et al., (2023). (add better citation). <br>
Handling multiple runs: For datasets that have multiple runs/subject, the outputs described below are generated for each run. Additionally, run-level maps are combined with a fixed-effects model (this amounts to averaging over runs, precision weighting is not done). <br>
Other notes: <br>
- Event durations are fixed to 1s for all tasks. <br>
- No scrubbing is done to remove high-motion volumes.

## Outputs for each subject in a given dataset:
- For each task:
    - Design matrix (.png and .csv file)
    - The model residuals (.nii.gz file)
    - Contrast map for each contrast (z-scores, image file with a z-score=2 plotting cutoff and a .nii.gz file)
    - Diagnostics: variance inflation factor (VIF) calculated for each contrast

## Analysis scripts and example outputs
Eventually this repo will have an analysis script for each dataset that was processed. For now, see example.py for a generic processing pipeline. See also example_design_matrix.png and example_statmap.png generated for one subject from this dataset. 
