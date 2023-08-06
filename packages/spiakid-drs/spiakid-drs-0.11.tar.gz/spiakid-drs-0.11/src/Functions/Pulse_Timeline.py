import numpy as np
import Functions.utility as ut
import Functions.IQCalibration as IQCal

class Pulse_Timeline(object):
    r"""Read the Pulse IQ timeline and give back main information on each measurement.
    
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

    The following attributes are automatically calculated and added during initialization.

    Attributes
    ----------
    **timeline**: dictionnary
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

    **single_pulse**: dictionnary
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
 
    def __init__(self,IQ,data,res,t_offset = 0,binsize = 0):
        self.timeline = {}
        self.single_pulse = {}
        self.timeline['IQ'] = IQ
        Pulse_Timeline.Average(self,data,res,binsize,t_offset)
        
    def Average(self,data,res,binsize,t_offset,calibrate_drift=True):
            #Reading data from the file
            I = self.timeline['IQ'][0] * data['vgains'][0] + data['voffsets'][0] 
            Q = self.timeline['IQ'][1] * data['vgains'][1] + data['voffsets'][1]
            #Finding where is the resonance frequency
            resfreqindx = np.argmin(np.abs(res.freq-data['measfreq']))
            #Data at the resonance frequency
            Ip_initial = res.I[resfreqindx]
            Qp_initial = res.Q[resfreqindx]
            dt = 1/data['samplefreq']
            #Cutting all the pulses
            Ip,Qp,pulseIRaws,pulseQRaws = Pulse_Timeline.GenAveragePulse(I,Q,dt = dt,pulsefreq = data['laserfreq'],t_offset = t_offset)
            t_seg = np.arange(0,len(Ip))*dt
            pulse_avg = np.zeros([2,int(len(Ip)/binsize)])   # Amplitude, Phase
            pulse_avg_IQ = np.zeros([2,int(len(Ip)/binsize)]) 
            #for each pulse
            for pulseindx in range(len(pulseIRaws)):
                self.single_pulse['pulse%d'%(pulseindx)] = {}
                #Taking data of this pulse
                Iv = pulseIRaws[pulseindx]
                Qv = pulseQRaws[pulseindx]
                points = int((1/data['laserfreq']/2 - t_offset)/dt)
                #Calibration if there is a drift
                if calibrate_drift:
                    Iv = Iv - np.mean(Iv[0:points]) + Ip_initial
                    Qv = Qv - np.mean(Qv[0:points]) + Qp_initial
                #Reduction of the number of point
                self.timeline['t'],Iv_bined = ut.AverageArray(t_seg,Iv,chuncksize = binsize)
                self.timeline['t'],Qv_bined = ut.AverageArray(t_seg,Qv,chuncksize = binsize)
                self.single_pulse['pulse%d'%(pulseindx)]['I'] = Iv_bined
                self.single_pulse['pulse%d'%(pulseindx)]['Q'] = Qv_bined
                #Calibration of the transmission
                pulse_amp,pulse_phase = res.cal_pulse_outside(Iv_bined + 1j*Qv_bined,data['measfreq'])
                avenum = int((1/data['laserfreq']/2 - t_offset)/binsize/dt)
                #Putting back in radians
                pulse_phase = np.unwrap(pulse_phase) *180 / np.pi
                #If >360, putting back at 0
                pulse_phase = np.where(pulse_phase<0,pulse_phase,pulse_phase-360)
                phase0 = np.mean(pulse_phase[0:avenum])
                self.single_pulse['pulse%d'%(pulseindx)]['Phase'] = (pulse_phase-phase0)
                pulse_amp = pulse_amp * 180/np.pi
                amp0 = np.mean(pulse_amp[0:avenum])
                self.single_pulse['pulse%d'%(pulseindx)]['Amplitude'] = (pulse_amp-amp0)
                pulse_avg_IQ[0,:] = pulse_avg_IQ[0,:] + self.single_pulse['pulse%d'%(pulseindx)]['I']
                pulse_avg_IQ[1,:] = pulse_avg_IQ[1,:] + self.single_pulse['pulse%d'%(pulseindx)]['Q']
                pulse_avg[0,:] = pulse_avg[0,:] + self.single_pulse['pulse%d'%(pulseindx)]['Amplitude']
                pulse_avg[1,:] = pulse_avg[1,:] + self.single_pulse['pulse%d'%(pulseindx)]['Phase']

            self.timeline['pulse_avg'] = pulse_avg / data['groupnum']
            self.timeline['pulse_avg_IQ'] = pulse_avg_IQ / data['groupnum']
            
            index = np.argmin(self.timeline['pulse_avg'][1,:])
            t = self.timeline['t']
            liste_pulse = []
            
            # Computing the average exponential decay of the timeline
            for key,value in self.single_pulse.items():
                liste_pulse.append(key)
            
            coeff = ut.fit_decay(self.timeline['pulse_avg'][1,:],t,index)
            self.timeline['decay'] = coeff[2]
            self.timeline['const'] = coeff[0]
            amp = []
            
            for pulseindx in range(len(liste_pulse)):
                
                coeff = ut.fit(self.single_pulse['pulse%d'%(pulseindx)]['Phase'], t, self.timeline['decay'],index)
                amp.append(coeff[1])
            self.timeline['fit_amp'] = np.mean(amp)

      

    def GenAveragePulse(I,Q,dt = 1e-8,pulsefreq = 250,t_offset = 0,segtime = 0):
                NumPointPulse = round(1/pulsefreq/dt)
                
                Pointoffset = round(t_offset/dt)
                
                pulseNum = int((len(I)-Pointoffset)/NumPointPulse)
                
                pulseIRaws = []
                pulseQRaws = []
                
                if segtime > 0 and segtime<1/pulsefreq:
                    segpoints = round(segtime/dt)
                    
                else:
                    segpoints = NumPointPulse
                    
                pulseI = np.zeros(segpoints);
                pulseQ = np.zeros(segpoints);    
                    
                
                for i in range(pulseNum):
                    
                    I_current = I[(i*NumPointPulse+Pointoffset):(i*NumPointPulse+Pointoffset+segpoints)]
                    Q_current = Q[(i*NumPointPulse+Pointoffset):(i*NumPointPulse+Pointoffset+segpoints)]
                    pulseIRaws.append(I_current)
                    pulseQRaws.append(Q_current)
                    
                    pulseI = pulseI + I_current
                    pulseQ = pulseQ + Q_current
                    

                    
                pulseI = pulseI/pulseNum
                pulseQ = pulseQ/pulseNum
                
                return pulseI, pulseQ, pulseIRaws,pulseQRaws
    
