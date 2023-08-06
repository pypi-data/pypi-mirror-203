import numpy as np
import re
import scipy as sp
import os
import pickle
from scipy.optimize import least_squares
import Functions.IQCalibration as IQCal


""""
Functions used in diffrent codes
"""

#Find A,B,delta in A+Bexp(delta*x)
def fit_decay(data,t,index):
        def model_decay(x,u):
            return x[0] + x[1] * np.exp(u*x[2])

        def fun_decay(x,u,y):
            return model_decay(x,u) - y

        def Jac_decay(x,u,y):
            J = np.empty((u.size,x.size))
            J[:,0] = 1
            J[:,1] = np.exp(u * x[2])
            J[:,2] = u * x[1] * np.exp(u * x[2])
            return J

        dat = np.array(data[index:])
        time = np.array(t[index:])  
        x0 = np.array([1e-03,0,-7e+04])
        res = least_squares(fun_decay, x0, jac=Jac_decay, args=(time-t[index], dat))
        return np.array([res.x[0],res.x[1],res.x[2]])

#find A,B in A+Bexp(delta*x) with delta given
def fit(data, t, decay,index):
        def model(x,u):
            return x[0] + x[1] * np.exp(u * decay)
        def fun(x,u,y):
            return model(x,u) - y

        def Jac(x,u,y):
            J = np.empty((u.size,x.size))
            J[:,0] = 1
            J[:,1] = np.exp(u * decay)
            return J
        dat = np.array(data[index:])
        time = np.array(t[index:])
        x0 = np.array([0,0.5])
        res = least_squares(fun, x0, jac=Jac, args=(time-t[index], dat))
        # plt.figure(0)
        # plt.scatter(t,data)
        # plt.plot(time,res.x[0]+res.x[1]*np.exp(decay * (time-t[index])),'--',c='r')
        # plt.title('c='+str(res.x[0])+' & amp='+str(res.x[1]*180/np.pi))
        # plt.xlabel('Time')
        # plt.ylabel('Pulse degree')
        # plt.show()
        return res.x[0],res.x[1]

#Fit a Gaussian
def Gaussian(x,a,mu,sigma):
    return a/sigma/np.sqrt(2*np.pi)*np.exp(-(x-mu)**2/2/sigma**2)

def covariance_from_psd(psd, size=None, window=None, dt=1.):
    autocovariance = np.real(np.fft.irfft(psd / 2., window) / dt)  # divide by 2 for single sided PSD
    if size is not None:
        autocovariance = autocovariance[:size]
    covariance = sp.linalg.toeplitz(autocovariance)
    return covariance

def CombineBins(freq,spectrum,bins = [50,1e3,1e4,1e5,1e6],resolutions = [1,10,100,1000,10000]):
    
    indx_bins = []
    
    indx_bins.append(0)
    
    for i,freqseg in enumerate(bins):
        
        indx_bin = np.argmin(np.abs(freq-freqseg))
        
        if indx_bin == len(freq): #check if the bin is the end of the freq
            
            if indx_bins[i-1] == indx_bin:
                
                break
            
        indx_bins.append(indx_bin)
        
        
    if indx_bins[-1] < len(freq)-1: #check if the bin is the end of the freq
        
        bins.append(freq[-1])
         
        indx_bins.append(len(freq))
        
        resolutions.append(resolutions[-1])
        
    if len(bins) > len(indx_bins):
        
        bins = bins[0:len(indx_bins)]
        resolutions = resolutions[0:len(indx_bins)]
    
    
    df = freq[1]-freq[0]
    
    NumBinned = 0
    
    NumBins = []
    
    for i, freqseg in enumerate(bins):
        
        resolution = resolutions[i]
        
        if df > resolutions[i]:
            
            resolution = df
        
        if i == 0:
            NumBinned = NumBinned + np.floor(freqseg/resolution)
            NumBins.append(np.floor(freqseg/resolution))
        else:
            NumBinned = NumBinned + np.floor((freqseg - bins[i-1])/resolution)
            NumBins.append(np.floor((freqseg - bins[i-1])/resolution))
        
        # NumBins.append(NumBinned)
            
    freq_binned = np.zeros(int(NumBinned))
    
    spectrum_binned = np.zeros(int(NumBinned))
        
    
    count = 0
    
    for i, freqseg in enumerate(bins):
        
        resolution = resolutions[i]
        
        indx = indx_bins[i]
            
        if df > resolutions[i]:
            
            resolution = df
            
        # Numbin = int(np.floor(freqseg / resolution))
        
        Numbin = int(NumBins[i]) - 1
            
        Bincombine = int(np.floor(resolution/df))
            
        for jN in range(Numbin):
                
             freq_binned[count] = freq[indx + jN*Bincombine] 
             spectrum_binned[count] = np.sum(spectrum[indx+jN*Bincombine:indx+(jN+1)*Bincombine])/Bincombine
             
             count = count + 1
             
             
             
        
    return freq_binned[0:count],spectrum_binned[0:count]    

def ExtractDatafromString(data_string):
    
    data_string = re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[+-]?\ *[0-9]+)?',data_string)
    
#    data_string = re.findall('-?\d\.?\d*[Ee][+\-]?\d+',data_string);
    
    data = [float(i) for i in data_string]
    
    return data

def AverageArray(time,array,chuncksize = 10):
    
    newarraysize = int(np.floor(len(array)/chuncksize));
    newarray = np.zeros(newarraysize)
    newtimearray = np.zeros(newarraysize)
    for i in range(newarraysize):
        newarray[i] = np.mean(array[i*chuncksize:(i+1)*chuncksize])
        newtimearray[i] = time[i*chuncksize]
        
    return newtimearray,newarray
             
def GenReslist(datafolder,select_by = "Temp",InAtten = 30,Temp = 50,IDString = ["_cal.obj"]):

    reslist = []
    resfreq = []
    temp = []
    resfilenames = []
    
    
    if select_by == "Temp":
        
        AttenString = "Inatten{0:.0f}".format(InAtten)
        
        IDString.append(AttenString)
        
        folders = os.listdir(datafolder)
        
        tempfolders = []
        
        #Get the temp folders
        for folder in folders:
            
            if "mK" in folder and os.path.isdir(datafolder + "//" + folder): 
                
                tempfolders.append(datafolder + "//" + folder)
                
        # print(tempfolders)
                
        #Get the res filenames        
        for folder in tempfolders:
            
            files = os.listdir(folder)
            
            
            
            for file in files:
                
                correct_file = True
                
                for string in IDString:
                
                    correct_file = correct_file*(string in file)
                
                if correct_file:
                    resfilenames.append(folder + "//" + file)
        
                
        if resfilenames != []:
            
            # print(resfilenames)
            for file in resfilenames:
            
                f = open(file,'rb')
                res = pickle.load(f)
                f.close()
                
                reslist.append(res)
                
                temp.append(res.temp)
                
                resfreq.append(res.lmfit_vals[1])
                
            indxs = np.argsort(np.array(temp))    
            
            temp = [temp[k] for k in indxs]
            resfreq = [resfreq[k] for k in indxs]
            reslist = [reslist[k] for k in indxs]
                
    return temp,resfreq,reslist                  
                
def GenReslistobj(datafolder,select_by = "temp",InAtten = 30,Temp = 50,
                  AttenStringFormat = "Inatten{0:.0f}",TempStringFormat = "Res{0:.0f}mK",IDString = [".obj"]):

    reslist = []
    resfreq = []
    temp = []
    resfilenames = []
    
    
    if select_by == "temp":

        AttenString = AttenStringFormat.format(InAtten)
        
        IDString.append(AttenString)
        
        folders = os.listdir(datafolder)
        
        tempfolders = []
        
        #Get the temp folders
        for folder in folders:
            
            if "mK" in folder and os.path.isdir(datafolder + "//" + folder): 
                
                tempfolders.append(datafolder + "//" + folder)
        #Get the res filenames        
        for folder in tempfolders:
            
            files = os.listdir(folder)
            
            
            
            for file in files:
                
                correct_file = True
                
                for string in IDString:
                
                    correct_file = correct_file*(string in file)
                
                if correct_file:
                    resfilenames.append(folder + "//" + file)
        
                
        if resfilenames != []:
            for file in resfilenames:
            
                f = open(file,'rb')
                res = pickle.load(f)
                f.close()
                
                reslist.append(res)
                
                temp.append(res.temp)
                
                resfreq.append(res.lmfit_vals[1])
                
            indxs = np.argsort(np.array(temp))    
            
            temp = [temp[k] for k in indxs]
            resfreq = [resfreq[k] for k in indxs]
            reslist = [reslist[k] for k in indxs]
    
    if select_by == "pwr":
        
        TempString = TempStringFormat.format(Temp)
        
        IDString.append(TempString)
        
        folders = os.listdir(datafolder)
        
        tempfolders = []
        
        #Get the temp folders
        for folder in folders:
            
            if "mK" in folder and os.path.isdir(datafolder + "//" + folder): 
                
                tempfolders.append(datafolder + "//" + folder)
        #Get the res filenames        
        for folder in tempfolders:
            
            files = os.listdir(folder)

            for file in files:
                
                correct_file = True
                
                for string in IDString:
                
                    correct_file = correct_file*(string in file)
                
                if correct_file:
                    resfilenames.append(folder + "//" + file)
        
                
        if resfilenames != []:
            for file in resfilenames:
            
                f = open(file,'rb')
                res = pickle.load(f)
                f.close()
                
                reslist.append(res)
                
                temp.append(res.temp)
                
                resfreq.append(res.lmfit_vals[1])
                
            indxs = np.argsort(np.array(temp))    
            
            temp = [temp[k] for k in indxs]
            resfreq = [resfreq[k] for k in indxs]
            reslist = [reslist[k] for k in indxs]
    
    
    
    
    
    return temp,resfreq,reslist, resfilenames                               

def ExtractLmfitParams(reslist,param = 'f0'):
    
    if param in reslist[0].lmfit_labels:
        indx = reslist[0].lmfit_labels.index(param)
    else:
        print("No %s in the reslist" %(param))
        return [];
    
    params = []
    
    for res in reslist:
        
        params.append(res.lmfit_vals[indx])

    return params

def GetSortIndex(params,desending = True):
    
    indx = sorted(range(len(params)), key=lambda k: params[k])
    
    if desending == False:
        indx.reverse()
    
    return indx
          
def GetResTemp(folder,tempindx = 0):
    
    files = os.listdir(folder)
    
    temps = []
    for file in files:
        
        params = ExtractDatafromString(file)
        
        temps.append(params[tempindx])
        
    return temps
         
def CalPowerResponse(oresponse,opower):

    oresponse = np.array(oresponse)
    opower = np.array(opower)
    
    response = []
    
    for i in range(oresponse.shape[1]):
        
        oresponse_i = oresponse[:,i]
        
        fitresult = np.polyfit(opower,oresponse_i,1)
        
        response.append(fitresult[0])
        
        
    return response
 
def fit_sin(t,A,phi,I0,f):

    return A*np.sin(2*np.pi*f*t + phi) + I0

def fit_cos(t,A,phi,I0,f):
    
    return A*np.cos(2*np.pi*f*t + phi) + I0



