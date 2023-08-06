import numpy as np
import Functions.Pulse_Timeline as pt


class Pulse_average(object):
    r"""


    Parameter
    ---------
    IQ: array (To check)
        The IQ data from the file.
    
    res: object
        The resonator modelisation of the pixel.
    
    t_offset: float (optional)
        To move the trigger time of the pulse. t_offset = 0 means the trigger of the pulse is in the center.

    binsize: int   
        The average data number.

    Attributes
    ----------

    **avg**: dictionnary
        Contains information on the average of pulses from every measurment
        
        - I: array
            The in-phase (or real part) of the complex S21 measurement
        - Q: array
            The out-of-phase (or imaginary part) of the complex S21 measurement
        - amp: array
        - phase: array

    **single_timeline**: dictionnary
        Contains information on each pulse in each mesurement

        - timeline: dictionnary
            Contains information about the average of every pulse from IQ.

            - IQ: array (To check)
                The IQ data from the file
        
            - t: array 
                Time of measurment
        
            - pulse_avg: array
                Average of all the pulse from IQ. Contains amplitude and phase.

            - pulse_avg_IQ: array
                Average of all the pulse from IQ. Contains I and Q
        
            - const: float
                Constant of the exponential fitting (const + A * exp(decay*x))

            - fit_amp: float
                Amplitude of the exponential fitting (const + A * exp(decay*x))

            - decay: float  
                Exponant of the exponential fitting (const + A * exp(decay*x))

        - single_pulse: dictionnary
            Contains each pulse from IQ.

            - pulse0: dictionnary
                Contains information about the pulse 0 (to 123)
                
                - I: array
                    The in-phase (or real part) of the complex S21 measurement
                - Q: array
                    The out-of-phase (or imaginary part) of the complex S21 measurement
                - Phase: array
                - Amplitude: array

    """

    def __init__(self,res,data,t_offset,binsize):
        self.avg = {}
        pulse_avg = np.zeros([2,int(round(1/data['laserfreq']*data['samplefreq'])/binsize)])
        pulse_avg_IQ = np.zeros([2,int(round(1/data['laserfreq']*data['samplefreq'])/binsize)])
        self.single_timeline = {}
        for i in range(data['groupnum']):
            print('i = ',i,'/',data['groupnum'])
            #Taking data on each pulse
            self.single_timeline['IQ%d'%(i)] = pt.Pulse_Timeline(data['IQ%d'%(i)],data,res,t_offset,binsize)
            pulse_avg = pulse_avg + self.single_timeline['IQ%d'%(i)].timeline['pulse_avg']
            pulse_avg_IQ = pulse_avg_IQ + self.single_timeline['IQ%d'%(i)].timeline['pulse_avg_IQ']
        pulse_avg_IQ = pulse_avg_IQ / data['groupnum'] 
        pulse_avg = pulse_avg / data['groupnum']   # I, Q, Amplitude, Phase
        self.avg['I'] = pulse_avg_IQ[0,:]
        self.avg['Q'] = pulse_avg_IQ[1,:]
        self.avg['amp'] = pulse_avg[0,:]
        self.avg['phase'] = pulse_avg[1,:]
        self.avg['t'] = self.single_timeline['IQ%d'%(i)].timeline['t']
  
