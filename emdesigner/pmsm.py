# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/06_pmsm.ipynb.

# %% auto 0
__all__ = ['pmsm']

# %% ../nbs/06_pmsm.ipynb 4
import numpy as np
from PIL import Image
from .stator import stator
from .rotor import rotor

# %% ../nbs/06_pmsm.ipynb 6
class pmsm(stator, rotor):
    def __init__(self, s = stator(), r = rotor()):
        self.stator = s
        self.rotor = r
        self.airgap = 0
        self.valid = False
    
    def valid_design(self):
        if self.airgap <= 0:
            print('motor airgap cannot be negative or zero')
            return 0
        
        self.valid = True
        
        

