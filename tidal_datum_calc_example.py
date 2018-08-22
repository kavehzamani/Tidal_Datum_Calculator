import numpy as np
import scipy
import matplotlib.pyplot as plt
################################################
from scipy.signal import argrelextrema
#################################################
# input: 
# ts, time series of a tidal wave 
# outpout:
# MTL,MHHW,MHW,MLW,MLLW, tidal water levels (see their definitions in NOAA
# Tides and Currents webpage)

dummy_x = np.arange (-17,18,0.1)
ts = np.sin(dummy_x ) + np.sin(2*dummy_x)  +3

plt.plot(dummy_x,ts,'r--',linewidth=2.0) ##
plt.grid() ##
plt.show() ##

# find mean
MTL = ts.mean()
# find peak location and anti peak location
pks_loc = argrelextrema(ts, np.greater)
a_pks_loc = argrelextrema(-ts, np.greater)
# find peak and anti_peak
pks = ts[pks_loc]
apks = ts[a_pks_loc]
# select every one another
pks_odd = pks[::2]
pks_even = pks[1::2]
apks_odd = apks[::2]
apks_even = apks[1::2]
##
if len(pks_odd)==len(pks_even):
    dummy_1 = np.maximum(pks_odd,pks_even)
    dummy_2 = np.minimum(pks_odd,pks_even)
elif len(pks_odd)>len(pks_even):
    #pks_even.insert(len(pks_even),pks_even[-1])
    pks_even = np.append(pks_even,pks_even[-1]) 
    dummy_1 = np.maximum(pks_odd,pks_even)
    dummy_2 = np.minimum(pks_odd,pks_even)
else:
    #pks_odd.insert(len(pks_odd),pks_odd[-1])
    pks_odd = np.append(pks_odd,pks_odd[-1]) 
    dummy_1 = np.maximum(pks_odd,pks_even)
    dummy_2 = np.minimum(pks_odd,pks_even)

MHHW = dummy_1.mean()
MHW = dummy_2.mean()
##
if len(apks_odd)==len(apks_even):
    dummy_3 = np.maximum(-apks_odd,-apks_even)
    dummy_4 = np.minimum(-apks_odd,-apks_even)
elif len(apks_odd)>len(apks_even):
     apks_even = np.append(apks_even,apks_even[-1]) 
     dummy_3 = np.maximum(-apks_odd,-apks_even)
     dummy_4 = np.minimum(-apks_odd,-apks_even)
else:
    apks_odd = np.append(apks_odd,apks_odd[-1])
    dummy_3 = np.maximum(-apks_odd,-apks_even)
    dummy_4 = np.minimum(-apks_odd,-apks_even)

MLW = -dummy_4.mean()
MLLW = -dummy_3.mean()

