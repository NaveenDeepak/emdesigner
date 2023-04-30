# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_rotor.ipynb.

# %% auto 0
__all__ = ['rotor']

# %% ../nbs/05_rotor.ipynb 3
import numpy as np
from PIL import Image

# %% ../nbs/05_rotor.ipynb 6
class rotor:
    def __init__(self):
        self.poles = 0
        self.outerdiameter = 0
        self.innerdiameter_fraction = 0
        self.poleembrace = 0
        self.magnetthickness_fraction = 0
        self.stacklength = 0 
        self.magnetgrade = 0
        self.steel_grade = 0
        self.valid = False
        self.params = 0
    
    def valid_design(self):

        # check number of slots
        if self.poles <= 0 or self.poles%2 != 0:
            print('Invalid rotor poles for electric motor')
            return 0
        
        # verify stator outer diameter
        if self.outerdiameter <= 0:
            print('Invalid rotor outer diameter')
            return 0
        
        self.calculate_parameters()

        self.valid = True
    
    def calculate_parameters(self):
        """calculate dimensions requied for calculation rotor properties
        """
        Rro = self.outerdiameter/2
        Rri = Rro*self.innerdiameter_fraction
        lm = (Rro - Rri)*self.magnetthickness_fraction
        a_m = self.poleembrace
        Am = np.pi*(Rro**2 - Rri**2)*self.poleembrace
        th_p = np.pi*2/self.poles
        self.params = {'Rro': Rro,
                        'Rri': Rri,
                        'lm': lm,
                        'a_m': a_m,
                        'Am': Am,
                        'th_p': th_p}    

