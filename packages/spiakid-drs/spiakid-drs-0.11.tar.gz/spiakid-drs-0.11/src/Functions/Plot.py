import numpy as np
import matplotlib.pyplot as plt
import Functions.utility as ut



def Pulse_Height(data, binsize, Format, savefolder):
    #Histogram with all the pulse height according to the phase
    pulseheight = np.array(data.pixel['pulse_height'])
    pmin = np.min(-pulseheight)
    pmax = np.max(-pulseheight)
    bins = np.arange(pmin,pmax+binsize ,binsize)
    plt.figure()
    plt.hist(-pulseheight,bins)
    plt.xlabel('Pulse Height(deg)')
    plt.ylabel('Counts')
    plt.savefig(savefolder + '/Pulse_Height'+Format,bbox_inches = 'tight')
    plt.close()

def Energy_Resolution(data, binsize, photonum, Format, savefolder):
    #Pulse Height Histogram and the fitting gaussians
    pulseheight = np.array(data.pixel['pulse_height'])
    pmin = np.min(-pulseheight)
    pmax = np.max(-pulseheight)
    bins = np.arange(pmin,pmax+binsize ,binsize)
    a = np.histogram(-pulseheight,bins)
    out = data.pixel['out']
    x = a[1]
    x = x[:-1]
    plt.figure()
    plt.hist(-pulseheight,bins)
    plt.xlabel('Pulse Height(deg)')
    plt.ylabel('Counts')
    #computing gaussians
    for i in range(photonum):
        amp = out.best_values['g%d_amplitude'%(i)]
        center = out.best_values['g%d_center'%(i)]
        sigma = out.best_values['g%d_sigma'%(i)]
        
        y = ut.Gaussian(x,amp,center,sigma)
        plt.plot()
        plt.plot(x+binsize/2,y,'--',linewidth = 3,color = 'red',alpha = 0.5)
        
        peak = amp/sigma/np.sqrt(2*np.pi)
    
        plt.text(center + 0.5,peak+2,'n=%d'%(i),fontsize = 18)
        
        
        g0_center = out.best_values['g0_center']
        g1_center = out.best_values['g1_center']
        
        sigma1 = out.best_values['g1_sigma']
        #Computing Resolution
        R = 1/2/np.sqrt(2*np.log(2)) * (g1_center-g0_center)/sigma1

        
        plt.annotate('$\\frac{E}{\Delta E}$' + '= %1.1f @ n=1' %(R), xy=(1,1), xytext=(-130, -12), va='top',
                 xycoords='axes fraction', textcoords='offset points',fontsize = 20)

    plt.savefig(savefolder + '/Energy_Resolution'+Format,bbox_inches = 'tight')
    plt.close()


def Avg_pulse(data, Format, savefolder, fit = False):
    #Plot of the average phase and amplitude according to the time
    t = data.pixel['Pulse'].avg['t']
    amp = data.pixel['Pulse'].avg['amp']
    phase = data.pixel['Pulse'].avg['phase']
    plt.figure()
    plt.plot(t,amp)
    plt.plot(t,phase)

    plt.xlabel('Time')
    plt.ylabel('Response')
    plt.title('Average Pulse')

    if fit:
        index = np.argmin(phase)
        pulseheight = np.array(data.pixel['pulse_height'])
        time = t[index:]
        avg = np.mean(pulseheight)
        plt.plot(time,data.pixel['const']+avg*np.exp(data.pixel['decay'] * (time-t[index])),'--',c='r')
    plt.savefig(savefolder + '/avedata' + Format ,bbox_inches = 'tight')

def Avg_pulse_timeline(data, IQ, level, Format, savefolder):
    #Plot the average of a measurment
    if level ==0:
        t = data.timeline['t']
        amp = data.timeline['pulse_avg'][0,:]
        phase = data.timeline['pulse_avg'][1,:]
    elif level ==1:
        t = data.single_timeline['IQ%d'%(IQ)].timeline['t']
        amp = data.single_timeline['IQ%d'%(IQ)].timeline['pulse_avg'][0,:]
        phase = data.single_timeline['IQ%d'%(IQ)].timeline['pulse_avg'][1,:]
    else:
        t = data.pixel['Pulse'].single_timeline['IQ%d'%(IQ)].timeline['t']
        amp = data.pixel['Pulse'].single_timeline['IQ%d'%(IQ)].timeline['pulse_avg'][0,:]
        phase = data.pixel['Pulse'].single_timeline['IQ%d'%(IQ)].timeline['pulse_avg'][1,:]
    
    index = np.argmin(phase)

    plt.figure()
    plt.plot(t,phase, label = 'Phase (deg)')
    plt.plot(t,amp, label = 'Amplitude')
    plt.legend()
    plt.savefig(savefolder + '/Avg_Pulse%d'%(IQ) + Format ,bbox_inches = 'tight')
    


def pulse_timeline(data, meas, IQ, level, Format, savefolder):
    #Plot a pulse
    if level ==0:
        t = data.timeline['t']
        amp = data.single_pulse['pulse%d'%(IQ)]['Amplitude']
        phase = data.single_pulse['pulse%d'%(IQ)]['Phase']
    elif level ==1:
        t = data.single_timeline['IQ%d'%(meas)].timeline['t']
        amp = data.single_timeline['IQ%d'%(meas)].single_pulse['pulse%d'%(IQ)]['Amplitude']
        phase = data.single_timeline['IQ%d'%(meas)].single_pulse['pulse%d'%(IQ)]['Phase']
    else:
        t = data.pixel['Pulse'].single_timeline['IQ%d'%(meas)].timeline['t']
        amp = data.pixel['Pulse'].single_timeline['IQ%d'%(meas)].single_pulse['pulse%d'%(IQ)]['Amplitude']
        phase = data.pixel['Pulse'].single_timeline['IQ%d'%(meas)].single_pulse['pulse%d'%(IQ)]['Phase']
    
    index = np.argmin(phase)
    time = t[index:]

    plt.figure()
    plt.plot(t,phase, label = 'Phase (deg)')
    plt.plot(t,amp, label = 'Amplitude')
    plt.legend()
    plt.savefig(savefolder + '/Meas%d'%(IQ) +'Pulse%d'%(meas)+ Format ,bbox_inches = 'tight')
    

