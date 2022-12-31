# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_cogging.ipynb.

# %% auto 0
__all__ = ['spm_embrace']

# %% ../nbs/03_cogging.ipynb 3
import numpy as np

# %% ../nbs/03_cogging.ipynb 5
def spm_embrace(s, r):
    """ This function calculates pole embrace with minimum cogging torque in SPM motor with 's' slots and 'r' poles
    """
    Nc = np.lcm(s, r)
    embrace_list = []
    embrace = 0
    j = 1
    while(embrace<1):
        embrace = round(j*r/Nc,3)
        embrace_list.append(embrace)
        j += 1
    
    return embrace_list

