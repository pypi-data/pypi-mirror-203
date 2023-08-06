"""Diagnostics for first-level GLM code: functions for analyzing the variance inflation factor (VIF),
modified from code written by Jeanette Mumford."""

import os
import pdb

import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
from scipy.stats import norm
from scipy.linalg import null_space



def est_vif(design_matrix):
    vif_data = pd.DataFrame()
    vif_data['regressor'] = design_matrix.columns.drop('constant')
    vif_data['VIF'] = [variance_inflation_factor(design_matrix.values, i)
                       for i, col in enumerate(design_matrix.columns) if col != 'constant']
    return vif_data

def est_contrast_vif(desmat, contrast, contrast_label):
    '''
    The goal of this function is to estimate a variance inflation factor for a contrast.
    This is done by extending the effective regressor definition from Smith et al (2007)
    Meaningful design and contrast estimability (NeuroImage).  Regressors involved
    in the contrast estimate are rotated to span the same space as the original space
    consisting of the effective regressor and and an orthogonal basis.  The rest of the 
    regressors are unchanged.
    input:
        desmat: design matrix.  Assumed to be a pandas dataframe with column  
             headings which are used define the contrast of interest
        contrast: a single contrast defined in string format
    output:
        vif: a single VIF for the contrast of interest  
    '''
    des_nuisance_regs = desmat[desmat.columns[contrast == 0]]
    des_contrast_regs = desmat[desmat.columns[contrast != 0]]

    con = np.atleast_2d(contrast[contrast != 0])
    con2_t = null_space(con)
    x = des_contrast_regs.copy().values
    q = np.linalg.pinv(x.T @ x)
    f1 = np.linalg.pinv(con @ q @ con.T)
    pc = con.T @ f1 @ con @ q
    con3_t = con2_t - pc @ con2_t
    f3 = np.linalg.pinv(con3_t.T @ q @ con3_t)
    eff_reg = x @ q @ con.T @ f1
    eff_reg = pd.DataFrame(eff_reg, columns = [contrast_label], index=desmat.index)

    other_reg = x @ q @ con3_t @ f3 
    other_reg_names = [f'orth_proj{val}' for val in range(other_reg.shape[1])]
    other_reg = pd.DataFrame(other_reg, columns = other_reg_names, index=desmat.index)

    des_for_vif = pd.concat([eff_reg, other_reg, des_nuisance_regs], axis = 1)
    vif_dat = est_vif(des_for_vif)
    vif_dat.rename(columns={'regressor': 'contrast'}, inplace=True)
    vif_output = vif_dat[vif_dat.contrast == contrast_label]
    # Also run regression on the design matrix to get stats on the coeffs.
    #X_labels = des_for_vif.columns.difference([contrast_label])
    #res = sm.OLS(des_for_vif[contrast_label], des_for_vif[X_labels]).fit()
    return vif_output['VIF'].values[0]

def est_all_contrast_vif(design_matrix, contrasts, contrast_labels, task_label, save_dir, run_ind):
    vif_stats = {'contrast': [],
                 'VIF': []}
    for con, con_label in zip(contrasts, contrast_labels):
        vif_out = est_contrast_vif(design_matrix, con, con_label)
        vif_stats['contrast'].append(con_label)
        vif_stats['VIF'].append(vif_out)
    vif_df = pd.DataFrame(vif_stats)
    vif_df.to_csv(os.path.join(save_dir, f'task-{task_label}_run-{run_ind+1}_diagnostics.csv'), index=False)
    return vif_df
