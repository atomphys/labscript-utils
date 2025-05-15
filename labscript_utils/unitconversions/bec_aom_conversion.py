#####################################################################
#                                                                   #
# bec_aom_conversion.py                                                       #
#                                                                   #
#                                                                   #
#####################################################################
from .UnitConversionBase import *

class bec_aom_conversion(UnitConversion):
    base_unit = 'V'
    derived_units = ['MHz','MHz_RF','Gammas']
    
    def __init__(self, calibration_parameters=None):            
        self.parameters = calibration_parameters
        
        self.parameters.setdefault('pass', 1)        # specify single- or double-pass with sign
        self.parameters.setdefault('gamma', 6.07)   # natural linewidth in MHz (Light)
        self.parameters.setdefault('VoltPerMHzRF', None)   # MHz per Volt (RF)
        self.parameters.setdefault('RFMHzOffset', None)   # MHz (RF) at 0V
        self.parameters.setdefault('aom_f0', None)      # rf frequency corrresponding to resonance in MHz (RF)
        
        
        
        
        
        UnitConversion.__init__(self,self.parameters)

    def MHz_RF_to_base(self, aom_RF_frequency_MHz):
        return (self.parameters['aom_f0']/self.parameters['pass']+aom_RF_frequency_MHz)*self.parameters['VoltPerMHzRF']
        
    def MHz_RF_from_base(self, volts):
        return volts/(self.parameters['VoltPerMHzRF'])-self.parameters['aom_f0']/self.parameters['pass']    
    
    
    def MHz_to_base(self, aom_frequency_MHz):
        return (self.parameters['aom_f0']+aom_frequency_MHz)*self.parameters['VoltPerMHzRF']/self.parameters['pass']
        
    def MHz_from_base(self, volts):
        return (volts/(self.parameters['VoltPerMHzRF']/self.parameters['pass'])-self.parameters['aom_f0'])
    
    
    def Gammas_to_base(self, gammas):
        return (self.parameters['aom_f0']+gammas*self.parameters['gamma'])*self.parameters['VoltPerMHzRF']/self.parameters['pass']
        
    def Gammas_from_base(self, volts):
        return (volts/(self.parameters['VoltPerMHzRF']/self.parameters['pass'])-self.parameters['aom_f0'])/self.parameters['gamma']
    
    
    
    
             
    # def linewidths_to_base(self, linewidths):
    #     aom_frequency = self.d_MHz_to_base(self.parameters['gamma'] * linewidths)
    #     return aom_frequency
        
    # def linewidths_from_base(self, aom_frequency):
    #     linewidths = self.d_MHz_from_base(aom_frequency) / self.parameters['gamma']
    #     return linewidths
