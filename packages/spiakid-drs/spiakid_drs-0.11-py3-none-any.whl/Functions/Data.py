import h5py

def read_hdf5(File_Path):
    """
    Read the hdf5 file and create a dictionnary
    """
    f = h5py.File(File_Path,'r')
    temp = f['header'].attrs['temp']    # Temperature
    pwr = f['header'].attrs['power']    # Power
    freq = f['resonator/freq'][...]     # Frequency
    I = f['resonator/I'][...]           # I of the resonator
    Q = f['resonator/Q'][...]           # Q of the resonator
    I0 = f['resonator/I0'][...]         # I when resonator is offline
    Q0 = f['resonator/Q0'][...]         # Q when resonator is offline
    IQCaldata = f['calibration/IQCaldata'][...] # Freq, Amp and Phase of calibration
    laserfreq = f['pulse'].attrs['laserfreq']   # Laser frequency
    samplefreq = f['pulse'].attrs['samplefreq'] # Samlpe frequency
    groupnum = f['pulse'].attrs['groupnum']     # Number of groups


    data ={
            "temp":temp,
            "pwr":pwr,
            "freq":freq,
            "I":I,
            "Q":Q,
            "I0":I0,
            "Q0":Q0,
            "IQCaldata":IQCaldata,
            'laserfreq':laserfreq,
            'samplefreq':samplefreq,
            'groupnum':groupnum}
    print('pulse')
    for i in range (groupnum):
        data['IQ%d'%(i)] = f['pulse']['IQ%d'%(i)][...]
    data['vgains']=f['pulse']['vgains'][...]    # Raw data from the oscilloscope
    data['voffsets']=f['pulse']['voffsets'][...]    # Raw data from the oscilloscope
    data['measfreq'] = f['pulse'].attrs['measfreq'] # Frequency sent to read out the resonance frequency
    data['nsamplefreq']=f['noise'].attrs['samplefreq']
    data['nmeasfreq']=f['noise'].attrs['measfreq']
    data['ngroupnum']=f['noise'].attrs['groupnum']
    data['nvoffsets']=f['noise']['voffsets'][...]
    data['nvgains']=f['noise']['vgains'][...]
    print('noise')
    for i in range (data['ngroupnum']):
        data['nIQ%d'%(i)] = f['noise']['IQ%d'%(i)][...]
    print('done')
    return data




