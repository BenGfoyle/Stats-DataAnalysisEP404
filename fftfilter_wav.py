#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EP404- fftfilter
Created on Wed Apr  3 12:54:15 2019

@author: mfc
"""

import numpy as np; pi=np.pi; pi2=2.0*pi
import random as rnd
from scipy.fftpack import fftfreq, fft, ifft
import matplotlib.pyplot as plt

def gaussgen(n,a,b):  
    normconst=1.0/np.sqrt(2.0*pi)
    total=0
    Store=np.zeros(n)
    rnd.seed(1234)
    i=0
    while i in range(n):
        total+=1
        x=12.0*rnd.random() - 6.0
        y=0.4*rnd.random()
        test = normconst*np.exp(-x**2/2.0)
        if(y<test):
            Store[i]=x*b+a
            i+=1        
    return Store
    
n = 40000
a=0.0
b=1.0    
Gauss=gaussgen(n,a,b)

Time=np.linspace(0,10,n)

Signal =  5.0*np.cos(128.0*pi2*Time)
Noise = 0.2*Gauss
SigNoise = Signal+5.0*Gauss


"""
#box-car integration
nbox=5 #width of sliding window
Boxsignal=np.zeros(n)
for i in range(n):
    boxsum=0.0
    for j in range(i,i+nbox):
        k=j
        if(j > (n-1)):k=j-n #periodic boundary condition
        boxsum=boxsum+SigNoise[k]
    boxsum=boxsum/nbox
    Boxsignal[i]=boxsum
"""

dt=Time[1]-Time[0]
Freq = fftfreq(n,dt)
F_signal = fft(SigNoise)

Cut_f_signal = F_signal.copy()
Cut_f_signal1 = F_signal.copy()
Cut_f_signal2 = F_signal.copy()
Cut_f_signal1[Freq > 260.0] = 0
Cut_f_signal1[Freq < 240.0] = 0 
Cut_f_signal2[Freq > -240.0]=0
Cut_f_signal2[Freq < -260.0]=0
Cut_f_signal=Cut_f_signal1 + Cut_f_signal2

Cut_signal=ifft(Cut_f_signal)

plt.subplot(221)
plt.plot(Time,Signal,lw=0.6)
plt.grid()
plt.ylabel("Amplitude")

plt.subplot(222)
plt.plot(Freq,abs(F_signal),lw=0.6)
plt.grid()

plt.subplot(224)
plt.plot(Freq,abs(Cut_f_signal),lw=0.6)
plt.grid()
plt.xlabel("Frequency (Hz)")

plt.subplot(223)
plt.plot(Time,abs(Cut_signal),lw=0.6)
plt.grid()
plt.xlabel("Time (sec)")
plt.ylabel("abs(Amplitude)")



############################################################################
import math
import wave
import struct

audio = []
#sample_rate = 44100.0
sample_rate=10000


def append_silence(duration_milliseconds=500):
    """
    Adding silence is easy - we add zeros to the end of our array
    """
    num_samples = duration_milliseconds * (sample_rate / 1000.0)
    for x in range(int(num_samples)): 
        audio.append(0.0)
    return

def append_sinewave(
        freq=440.0, 
        duration_milliseconds=500, 
        volume=1.0):

    global audio # using global variables isn't cool.

    num_samples = duration_milliseconds * (sample_rate / 1000.0)
    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * ( x / sample_rate )))
    return

def append_noise(Signal,
        freq=440.0, 
        duration_milliseconds=500, 
        volume=1.0):

    global audio # using global variables isn't cool.

    num_samples = duration_milliseconds * (sample_rate / 1000.0)
    Signal=Signal/(2.0*Signal.max())
    for x in range(int(num_samples)):
        audio.append(Signal[x])
    return

def save_wav(file_name):
    wav_file=wave.open(file_name,"w")
    nchannels = 1
    sampwidth = 2
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()
    return

append_sinewave()
append_silence(duration_milliseconds=500)
append_sinewave(freq=660)
append_silence(duration_milliseconds=500)
append_sinewave()
append_silence(duration_milliseconds=500)
append_noise(abs(5.0*Noise),volume=1.0,duration_milliseconds=4000)
append_silence(duration_milliseconds=1000)
append_noise(abs(5.0*Signal),volume=1.0,duration_milliseconds=4000)
append_silence(duration_milliseconds=1000)
append_noise(abs(5.0*SigNoise),volume=1.0,duration_milliseconds=4000)
append_silence(duration_milliseconds=1000)
append_noise(abs(5.0*Cut_signal),volume=1.0,duration_milliseconds=4000)
save_wav("output.wav")


