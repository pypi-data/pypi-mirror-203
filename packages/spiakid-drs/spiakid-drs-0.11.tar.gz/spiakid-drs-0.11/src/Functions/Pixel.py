import numpy as np
import scipy.signal as sg
from lmfit.models import GaussianModel

import Functions.utility as ut
import Functions.Pulse_average as pa


class Pixel(object):
    r"""Read the Pulse IQ timeline and give back main information on each measurment.

    Parameter
    ---------

    Data: dictionnary
        Data available from the hdf5 file about measurement.
    
    res: object
        The resonator modelisation of the sensor.
    
    t_offset: float (optional)
        To move the trigger time of the pulse. t_offset = 0 means the trigger of the pulse is in the center.

    binsize_pulse: int (optional)
        The average data number.
    
    binsize_hist: float (optional)
        Size of a bin in the histogram that will be used to fit the gaussian and compute the energy resolution
    
    photonum: int (optional)
        Number of peak to detect on the histogram (minimum 2)

    The following attributes are automatically computed and added during initialization.

    Attributes
    ----------

    - I0: array
        The in-phase (or real part) of the complex S21 measurement of the offset resonator

    - Q0: array
        The out-of-phase (or imaginary part) of the complex S21 measurement of the offset resonator

    - freq: array
        Frequency used to characterize the resonator

    - vgains: array
        Voltage gains of the oscilloscope

    - voffsets: array
        Offset of the oscilloscope

    - measfreq: float
        Frequency sent to the oscilloscope during measurement

    - pulse_height: array
        All the maximum around the pulse time

    - const: float
        Constant of the exponential fitting (const + A * exp(decay*x))

    - fit_amp: float
        Amplitude of the exponential fitting (const + A * exp(decay*x))

    - decay: float  
        Exponant of the exponential fitting (const + A * exp(decay*x))

    - out: object
        Contains information about the gaussian fittings
    
    - R: float
        The spectral resolution of the sensor
    
    - Pulse: dictionnary
        Contains information about pulses:

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

    def __init__(self,data,res, t_offset, binsize_pulse,binsize_hist, peakwidth, photonum):
        self.pixel = {}
        #the frequency of the trigger of the laser.
        self.pixel['pulselaser'] = data['laserfreq']
        #the data of the pulse is segmented. Load the number of the groups
        self.pixel['NumpulseUnscaled'] = data['groupnum']
        #load the sample frequency of the data. The usual sample rate is about 100MHz
        self.pixel['dt'] = 1/data['samplefreq']

        #load the DC offset of the IQ from the res
        self.pixel['I0'] = res.I0
        self.pixel['Q0'] = res.Q0
        self.pixel['freq'] = res.freq
        self.pixel['decay'] = []
        self.pixel['amp'] = []
        self.pixel['const'] = []
        #load the voltage gain and the offset of the oscilloscope 
        self.pixel['vgains'] = data['vgains']
        self.pixel['voffsets'] = data['voffsets']

        #load the readout tone frequency
        self.pixel['measfreq'] = data['measfreq']


        self.pixel['pulse_height'] = []
        self.pixel['out'] = []
        self.pixel['deltaEs'] = []
        self.pixel['Es'] = []
        self.pixel['sigmas'] = []
        self.pixel['R'] = 0

        # Compute information on every pulse
        self.pixel['Pulse'] = pa.Pulse_average(res,data,t_offset,binsize_pulse)

        # Compute information about the average pulse of every measurment
        Pixel.PulseStat(self,data,res,t_offset,binsize_pulse)

        # Compute information about the energy resolution of the resonator
        Pixel.resolution(self, binsize_hist, peakwidth, photonum)

    def PulseStat(self, data, res, t_offset, binsize):
        for i in range (self.pixel['NumpulseUnscaled']):    # Go in each measurment
            print('i: ',i,' / ',self.pixel['NumpulseUnscaled'])
            pulsedata = self.pixel['Pulse'].single_timeline['IQ%d'%(i)] # Compute information on every pulse
            index = np.argmin(pulsedata.timeline['pulse_avg'][1,:]) # Take the moment of the average pulse of the measurment
            t = pulsedata.timeline['t']
            time = np.array(t[index:])  
            liste_pulse = []
            # Computing the average exponential decay of the timeline
            for key,value in pulsedata.single_pulse.items():    
                liste_pulse.append(key)
            coeff = ut.fit_decay(pulsedata.timeline['pulse_avg'][1,:],t,index)
            decay = coeff[2]
            self.pixel['decay'].append(decay)
            self.pixel['const'].append(coeff[0])
            self.pixel['amp'].append(coeff[1])

            # Fit every pulse 
            for pulseindx in range(len(liste_pulse)):
                coeff = ut.fit(pulsedata.single_pulse['pulse%d'%(pulseindx)]['Phase'], t, decay,index)
                self.pixel['pulse_height'].append(coeff[1])
        self.pixel['decay'] = np.mean(self.pixel['decay'])
        self.pixel['amp'] = np.mean(self.pixel['amp'])
        self.pixel['const'] = np.mean(self.pixel['const'])
            
    def resolution(self, binsize, peakwidth,photonum):
        # Create histogram of pulseheight
        pulseheight = np.array(self.pixel['pulse_height'])
        pmin = np.min(-pulseheight)
        pmax = np.max(-pulseheight)
        bins = np.arange(pmin,pmax+binsize ,binsize)
        a = np.histogram(-pulseheight,bins)
        
        x = a[1]
        x = x[:-1]
        y = a[0]
        
        vals = sg.find_peaks(y,width = 6, distance = 10)    #Make a list of every peak
        # Take information on the first peak (0 photon)
        peaks_indx = vals[0]
        center0 = x[peaks_indx[0]]
        dpeak = x[peaks_indx[1]] - center0

        # Fit the Gaussian on peaks (to be checked)
        gaussmodes = []
        for peak in range(photonum):
            prefix = 'g%d_'%(peak)
            gauss = GaussianModel(prefix = 'g%d_'%(peak))
            if peak == 0:
                pars = gauss.make_params()
                pmin = np.min(y)
                pars[prefix + 'center'].set(center0,min = pmin,max = center0 + dpeak/2)
            else:
                pars.update(gauss.make_params())
                pars[prefix + 'center'].set(center0,min = center0 - dpeak/2,max = center0 + dpeak/2)
        
            center0 = center0 + dpeak
            pars[prefix + 'sigma'].set(1,min = 0.1,max = 2)
            pars[prefix + 'amplitude'].set(100,min = 0)
            gaussmodes.append(gauss)

            if peak == 0:
                mod = gauss
            else:
                mod = mod + gauss
        
        self.pixel['out'] = mod.fit(y, pars, x=x)   #information on every gaussian

        for i in range(photonum):
            amp = self.pixel['out'].best_values['g%d_amplitude'%(i)]
            center = self.pixel['out'].best_values['g%d_center'%(i)]
            sigma = self.pixel['out'].best_values['g%d_sigma'%(i)]
            y = ut.Gaussian(x,amp,center,sigma)
            self.pixel['deltaEs'].append(2*np.sqrt(2*np.log(2))*sigma)
            self.pixel['Es'].append(center)
            self.pixel['sigmas'].append(sigma)
        g0_center = self.pixel['out'].best_values['g0_center']
        g1_center = self.pixel['out'].best_values['g1_center']
        sigma1 = self.pixel['out'].best_values['g1_sigma']

        #Compute the enrgy resolution
        self.pixel['R'] = 1/2/np.sqrt(2*np.log(2)) * (g1_center-g0_center)/sigma1
