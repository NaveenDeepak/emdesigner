# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_stator.ipynb.

# %% auto 0
__all__ = ['stator']

# %% ../nbs/04_stator.ipynb 3
import numpy as np
from PIL import Image

# %% ../nbs/04_stator.ipynb 6
class stator:
    def __init__(self):
        self.slots = 0
        self.poles = 0
        self.outerdiameter = 0
        self.innerdiameter_fraction = 0
        self.slotopening_fraction = 0
        self.slot_shape = 'rectangle'
        self.shoeheight_fraction = 0
        self.toothwidth_fraction = 0
        self.backiron_fraction = 0
        self.stacklength = 0
        self.windinglayers = 0
        self.coilpitch = 0
        self.turns = 0
        self.strands = 0
        self.strand_dia = 0
        self.parallelpaths = 0
        self.steel_grade = 0
        self.valid = False
        self.dims = {}
    
    def valid_design(self):

        # check number of slots
        if self.slots < 0 or self.slots%3 != 0:
            print('Invalid stator slots for a 3phase machine')
            return 0
        
        # verify stator outer diameter
        if self.outerdiameter <= 0:
            print('Invalid stator outer diameter')
            return 0
        
        self.valid = True
    
    def calculate_parameters(self):
        """calculate dimensions requied for calculation of stator properties
        """
        Rso = self.outerdiameter/2
        Rsi = Rso*self.innerdiameter_fraction
        d1 = (Rso - Rsi)*self.shoeheight_fraction
        d2 = d1
        wbi = (Rso - Rsi - d1 - d2)*self.backiron_fraction
        d3 = (Rso - Rsi - d1 - d2 -wbi)
        th_s = np.pi*2/self.slots
        ws = 2*Rsi*np.sin(th_s*self.slotopening_fraction/2)
        wtb = 2*Rsi*np.sin(th_s*self.slotopening_fraction*self.toothwidth_fraction/2)
        wsi = (Rsi + d1 + d2) - wtb
        wsb = (Rsi + d1 + d2 + d3) - wtb
        As = (th_s*(Rsi + d1 + d2 + d3/2 ) - wtb)*d3/2

        # needs rotor information
        g = 1
        th_p = np.pi*2/self.poles
        Nspp = self.slots/(3*self.poles)
        a_cp = int(Nspp)/Nspp
        t_p = Rsi*th_p
        t_s = Rsi*th_s
        t_c = a_cp*t_p
        th_se = np.pi/(self.slots/self.poles)
        kd = np.sin(Nspp*th_se/2)/(Nspp*np.sin(th_se/2))
        lm = 4
        a_m = 0.83
        c_phi = 2*a_m/(1+a_m)
        gc = lm/(g*c_phi)
        kc_1 = (t_s/ws)*(5*gc/ws + 1)
        kc = 1/(1 - 1/kc_1)        

    
    def calculate_inductance(self):
        if self.valid:
            print('yet to be included')
        else:
            print('stator is invalid. please provide valid design using the valid_design() method')

