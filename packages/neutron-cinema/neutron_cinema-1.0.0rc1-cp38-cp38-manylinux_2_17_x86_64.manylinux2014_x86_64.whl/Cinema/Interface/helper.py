import numpy as np
from Cinema.Interface.units import *
import time
import multiprocessing
import os
from functools import partial
import h5py
import scipy


try:
    from pyfftw.interfaces import numpy_fft as fft
    import pyfftw
    pyfftw.interfaces.cache.enable()
    print('using pyfftw for fft')
except ImportError:
    from numpy import fft
    print('using numpy for fft')

#default units:
#energy eV
#wavelength angstrom
#time second
#wavenumber angstrom^-1
#angle degree
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy import interpolate

def takfft(input, dt=1., fftsize=None, conversion=2*np.pi):
    return fft.fftshift(fft.fft((input), n=fftsize))*dt/conversion

def takifft(input, dt=1., fftsize=None, conversion=2*np.pi):
    return fft.fftshift(fft.ifft((input), n=fftsize))/dt*conversion

def findData(fn, path='/', absPath=False):
    if not absPath:
        pxpath = os.getenv('TAKPATH')+ path
    for root, dirs, files in os.walk(pxpath):
        if fn in files:
            return os.path.join(root, fn)

def smooth(input, x):
    sample_rate = 100
    nyq_rate = sample_rate / 2.0
    width = 5.0/nyq_rate
    ripple_db = 100.0
    N, beta = kaiserord(ripple_db, width)
    cutoff_hz = 10.0
    taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
    filtered = lfilter(taps, 1.0, input)
    delay = 0.5 * (N-1) * (x[1]-x[0])
    f = interpolate.interp1d(x[N-1:]-delay , filtered[N-1:], fill_value= 'extrapolate' )
    return f(x)

def smoothVdos(vdos, omega, cut=0.):
    omegaflip = np.flip(omega)
    vdosflip = np.flip(vdos)

    x = np.concatenate((-omegaflip[:-1], omega))
    y = np.concatenate((vdosflip[:-1], vdos))

    ####################################
    sample_rate = 100
    nyq_rate = sample_rate / 2.0
    width = 10.0/nyq_rate
    ripple_db = 120.0 #in dB
    N, beta = kaiserord(ripple_db, width)
    cutoff_hz = 1.0
    taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
    filtered = lfilter(taps, 1.0, y)
    delay = 0.5 * (N-1) * (x[1]-x[0])
    f = interpolate.interp1d(x[12*N-1:]-delay , filtered[12*N-1:], fill_value= 'extrapolate' )
    if (cut):
        omegaSize = int(omega.size*cut)
        return  np.flip(f(omega))[:omegaSize], omega[:omegaSize]
    return (f(omega)), omega
    # return filtered[12*N-1:], x[12*N-1:]-delay


def angularFre2eKin(fre):
    return fre*radpsec2eV

def eKin2AngularFre(en):
    return en*eV2radpsec

def eKin2k(eV):
    return np.sqrt(eV*eV2kk)

def k2eKin(wn):
    return wn*wn/eV2kk

def q2Alpha(Q, kt):
    return Q*Q/(kt*eV2kk)

def alpha2Q(alpha,kt):
    return np.sqrt(alpha*kt*eV2kk)

def angle2Q(angle_deg, enin_eV, enout_eV):
    ratio = enout_eV/enin_eV
    k0=eKin2k(enin_eV)
    scale = np.sqrt(1.+ ratio - 2*np.cos(angle_deg*deg2rad) *np.sqrt(ratio) )
    return k0*scale

def angle2Alpha(angle, enin_eV, enout_eV, kt):
   return (enin_eV + enout_eV - 2*np.sqrt(enin_eV * enout_eV)*np.cos(angle*deg2rad))/kt

def nextGoodNumber(n):
    return int(2**np.ceil(np.log2(n)))

#fixme: slow
def calHKL(maxNum, jump=1):
    results = {results: [] for results in range(maxNum+1)}
    for h in range(0,maxNum,jump):  # half a space
        for k in range(-maxNum,maxNum,jump):
            for l in range(-maxNum,maxNum,jump):
                if h==0:
                    if k<0:
                        continue #half a plane
                    elif k==0 and l<=0: #half an axis and remove singularity
                        continue
                dis = np.sqrt(h*h + k*k + l*l)
                if dis>maxNum:
                    continue
                if np.abs(dis-round(dis)) < 1e-10:
                    results[int(dis)].append(np.array([h,k,l]))
    return results

