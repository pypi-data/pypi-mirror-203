import Functions.resonator as a
import Functions.cmplxIQ as fitmodel
import Functions.Pulse_Timeline as PT
import Functions.Pulse_average as PA
import Functions.Pixel as PX
import Functions.Data as dt
import Functions.Plot as pl

def Data_read(Data,Plot_path,Plot_Format,Plot_List,Level,meas,IQ_number):
    data = dt.read_hdf5(Data)
#get the temp and readout power of the measurement
    temp = data['temp']
    pwr = data['pwr']

#get frequency, I and Q of the resonator 
    freq = data['freq']
    I = data['I']
    Q = data['Q']

    I0 = data['I0']
    Q0 = data['Q0']

    #get the IQ calibation data for the noise and pulse data
    IQCaldata = data['IQCaldata']

    #create a resonator object
    res = a.Resonator('1', temp, pwr, freq, I, Q,I0 = I0,Q0 = Q0)
    #fit the resonator with S21 (transmission)
    res.load_params(fitmodel.cmplxIQ_params)
    res.do_lmfit(fitmodel.cmplxIQ_fit)

    t_offset = 0.001
    binsize_pulse = 500
    binsize_hist = 0.1

    templatetime = 0.002

    laserfreq = data['laserfreq']
    pulsetriggertime = 1/laserfreq/2 - t_offset
    savefolder = Plot_path
    samplefreq = data['samplefreq']
    #TODO Ask photonum on the interface
    if Level == 2:
        x = PX.Pixel(data,res,t_offset,binsize_pulse=500,binsize_hist=0.1,peakwidth=2,photonum=2)
    
    if Level == 1:
        x = PA.Pulse_average(res,data,t_offset,binsize_pulse)

    if Level == 0:
        x = PT.Pulse_Timeline(data['IQ%d'%(meas)],data,res,t_offset,binsize_pulse)


    if 0 in Plot_List:
        pl.Energy_Resolution(x,binsize_hist,photonum=2,Format=Plot_Format,savefolder=savefolder)
    if 1 in Plot_List:
        pl.Pulse_Height(x, binsize_hist, Format =Plot_Format, savefolder=savefolder)
    if 2 in Plot_List:
        pl.Avg_pulse(x, Format =Plot_Format, savefolder=savefolder, fit=True)
    if 3 in Plot_List:
        pl.Avg_pulse_timeline(x,meas,Level, Format =Plot_Format, savefolder=savefolder)
    if 4 in Plot_List:
        pl.pulse_timeline(x,meas,IQ_number,Level, Format =Plot_Format, savefolder=savefolder)
    





    #generate the averaged pulse data as the template
    # avedata = spp.GenPulseAverageWithHDF(res,f,savefolder,IQCaldata,calibrate_drift = True, t_offset = t_offset,savefig = True,Format=Plot_Format)

    # #generate the psd (Power Spectral Density) of the resonator
    # psd = spp.GenPSDWithHDF(res,f,savefolder,IQCaldata,binsize = binsize,pulselaser = laserfreq,Format=Plot_Format)


    # #generate the wiener filter for both amplitude and phase
    # wifilterphase, wifilteramp,indx = spp.GenWienerFilter(avedata,psd,savefolder,binsize = binsize,pulsetriggertime = pulsetriggertime,dt = 1/samplefreq, templatetime = templatetime,Format=Plot_Format)

    # #use the wiener filter to generate the pulse statistics
    # pulseheights = spp.GenPulseStatisticsHDF(res,f,wifilterphase,savefolder,IQCaldata,binsize = binsize,t_offset = t_offset,calibrate_drift = True,pulsetype = 'phase',plotbin = 0.2,Format=Plot_Format)

    # #estimate the energy resolution
    # spp.EnergyResolution(pulseheights,savefolder,photonum = 6,Format=Plot_Format)



