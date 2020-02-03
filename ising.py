#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Two-D Ising model
Created on Tue Mar 26 14:18:27 2019

@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

def initspin(n,spin):

    for i in range(n):
        for j in range(n):
            spin[i,j]=-1
            if (rnd.random() > 0.5): spin[i,j]=1
    return spin

def total_e(n,spin,h):
    energy = 0.0
    mag = 0.0
    eps = -1.0
 
    for i in range(n):
        for j in range(n):
            s=spin[i,j]
            mag=mag+s
            k1=i+1
            if(k1 == n): k1=0
            k2=i-1
            if(k2 < 0): k2=n-1
            k3=j+1
            if(k3 == n): k3=0
            k4=j-1
            if(k4 < 0): k4=n-1
            energy=energy+eps*s*(spin[k1,j]+spin[k2,j]+spin[i,k3]+spin[i,k4])

    #divide by 2 to allow for double counting of bonds
    energy=energy/2.0
    #add energy of interaction with external magnetic field
    energy=energy-h*mag
    return (energy,mag)

def flipspin(n,spin,h,beta,energy,mag):
    iflip = 0
    (energy,mag)=total_e(n,spin,h)
    e_old = energy
    mag_old = mag
    i=int(n*rnd.random())
    j=int(n*rnd.random())

    spin[i,j]=spin[i,j]*(-1.0)
    (energy,mag)=total_e(n,spin,h)
    e_new=energy
    mag_new=mag
    delE=e_new-e_old
    if(rnd.random() < np.exp(-1.0*beta*delE)):
        energy=e_new
        mag=mag_new
        iflip=1
    else:
        energy=e_old
        mag=mag_old
        spin[i,j]=spin[i,j]*(-1.0)
    
    return (spin,energy,mag,iflip)


n=8
spin=np.zeros([n,n])
nCycle=5000

Btemp=[]
Benergy=[]
Bmag=[]

fout=open('ising_out.dat','w')
iseed=1234
rnd.seed(iseed)

h=0.0
for kk in range(50):
    temp=(kk+1)*0.2
    print('......Ising: T = %10.5f \n' % temp)
    beta=1.0/temp
    spin = initspin(n,spin)
    energy,mag = total_e(n,spin,h)

    e_count=0
    m_count=0
    e_ave=0.0
    m_ave=0.0
    for i in range(nCycle):
        (spin,energy,mag,iflip) = flipspin(n,spin,h,beta,energy,mag)
        if(i > 1000):
            e_count=e_count+1
            m_count=m_count+1
            e_ave=e_ave+energy
            m_ave=m_ave+mag

    energy=e_ave/e_count
    mag=m_ave/m_count
    # next line required if examining (absolute) value of M as fn of T
    if(mag < 0.0): mag=mag*(-1.0)

    fout.write('%10.6f %10.6f %10.6f\n' % (temp,energy,mag))
    Btemp.append(temp)
    Benergy.append(energy)
    Bmag.append(mag)

fout.close()

fig1=plt.figure()
ax1=fig1.add_subplot(221)
ax1.plot(Btemp,Benergy, lw=0.8)
ax1.grid()
ax1.set_xlabel('Temperature')
ax1.set_ylabel('Energy')

ax1=fig1.add_subplot(223)
ax1.plot(Btemp,Bmag,lw=0.8)
ax1.grid()
ax1.set_xlabel('Temperature')
ax1.set_ylabel('Magnetisation')


