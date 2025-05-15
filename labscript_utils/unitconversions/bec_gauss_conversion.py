# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:42:30 2020

@author: BEC
"""


from __future__ import division, unicode_literals, print_function, absolute_import

from .UnitConversionBase import *
import numpy as np

class magnet (UnitConversion):
    base_unit = 'V'
    derived_units = ['G']
    
    def __init__(self, calibration_parameters=None):
        # These parameters are loaded from a globals.h5 type file automatically
        if calibration_parameters is None:
            calibration_parameters = {}
        self.parameters = calibration_parameters
        
        # I[A] = slope * V[V] + shift
        # Saturates at saturation Volts
        self.parameters.setdefault('slope', 1) 
        self.parameters.setdefault('shift', 0) # A
        self.parameters.setdefault('saturation', 10) # V
        
        UnitConversion.__init__(self,self.parameters)
        # We should probably also store some hardware limits here, and use them accordingly 
        # (or maybe load them from a globals file, or specify them in the connection table?)

    def G_to_base(self,gauss):
        #here is the calibration code that may use self.parameters
        volts = self.parameters['shift'] + gauss * self.parameters['slope']
        return volts
        
    def G_from_base(self,volts):
        volts = np.minimum(volts, self.parameters['saturation'])
        gauss = (volts - self.parameters['shift']) / self.parameters['slope']
        return gauss 
