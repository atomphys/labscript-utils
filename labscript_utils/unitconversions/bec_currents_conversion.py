from __future__ import division, unicode_literals, print_function, absolute_import

from .UnitConversionBase import *
import numpy as np

class linear_coil(UnitConversion):
    base_unit = 'V'
    derived_units = ['A', 'mA']
    
    def __init__(self, calibration_parameters=None):
        # These parameters are loaded from a globals.h5 type file automatically
        if calibration_parameters is None:
            calibration_parameters = {}
        self.parameters = calibration_parameters
        
        # I[A] = slope * V[V] + shift
        # Saturates at saturation Volts
        self.parameters.setdefault('slope', 1) # A/V
        self.parameters.setdefault('shift', 0) # A
        self.parameters.setdefault('saturation', 10) # V
        
        UnitConversion.__init__(self,self.parameters)
        # We should probably also store some hardware limits here, and use them accordingly 
        # (or maybe load them from a globals file, or specify them in the connection table?)

    def A_to_base(self,amps):
        #here is the calibration code that may use self.parameters
        volts =  self.parameters['shift'] + amps * self.parameters['slope']
        return volts
        
    def A_from_base(self,volts):
        volts = np.minimum(volts, self.parameters['saturation'])
        amps = (volts - self.parameters['shift']) / self.parameters['slope']
        return amps 
        
    def mA_to_base(self,amps):
        #here is the calibration code that may use self.parameters
        volts =  self.parameters['shift'] + amps * self.parameters['slope']
        return volts
        
    def mA_from_base(self,volts):
        volts = np.minimum(volts, self.parameters['saturation'])
        amps = (volts - self.parameters['shift']) / self.parameters['slope']
        return amps 
        
    