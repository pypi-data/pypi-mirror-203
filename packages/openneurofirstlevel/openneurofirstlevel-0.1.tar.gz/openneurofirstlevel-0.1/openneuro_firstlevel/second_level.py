import pdb
import os

import pandas as pd
from nilearn import image
from nilearn import plotting
from nilearn.glm import threshold_stats_img
from nilearn.glm.second_level import SecondLevelModel
import matplotlib.pyplot as plt



def run_second_level_analysis(save_dir, task_labels, contrast_labels, 
                              contrast_conditions, n_runs):
    # Aggregate all first-level maps
    subjects = pd.read_csv(os.path.join(save_dir, 'included_subjects.csv'))
    for task_label in task_labels:
        for con_label, contrast in zip(contrast_labels, contrast_conditions):
            save_label = f'task-{task_label}_contrast-{con_label}_second_level'
            first_level_maps = []
            for sub in subjects:
                sub_dir = os.path.join(save_dir, f'sub-{sub}') 
                if n_runs == 1:
                    map_fn = f'task-{task_label}_run-1_contrast-{con_label}_z_scores.nii.gz'
                else:
                    map_fn = f'task-{task_label}_run_avg_contrast-{con_label}_t_scores.nii.gz'
                first_level_maps.append(image.load_img(os.path.join(sub_dir, map_fn)))

            # Fit second-level model
            design_matrix = pd.DataFrame(
                [1] * len(first_level_maps), columns=['intercept'])
            second_level_model = SecondLevelModel(smoothing_fwhm=None)
            second_level_model = second_level_model.fit(
                first_level_maps, design_matrix=design_matrix)
            z_map = second_level_model.compute_contrast(output_type='z_score')
            thresholded_map1, threshold1 = threshold_stats_img(
                z_map, alpha=0.001, height_control='fpr',
                cluster_threshold=10, two_sided=True)

            z_fig = plt.figure(figsize=(12, 3))
            plotting.plot_stat_map(
                thresholded_map1,
                cut_coords=(-25, 0, 50),
                threshold=threshold1,
                figure=z_fig,
                title="Thresholded z map, fpr <.001, clusters > 10 voxels",
            )
            
            # Save
            plt.savefig(os.path.join(save_dir, f'{save_label}_zstatmap.png'))
            z_map.to_filename(os.path.join(save_dir, f'{save_label}_z_scores.nii.gz'))
