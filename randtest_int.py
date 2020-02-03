#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
randtest: Test file of random numbers for uniformity
version which modifies rnd.random() to use integer range [0-32768)
Created on Wed Jan  9 14:11:37 2019

@author: mfc
"""

import numpy as np
import matplotlib.pyplot as plt
plt.ion
plt.grid()

from math import factorial

n=100000
nn=10000
x=np.zeros(n)
bin1=np.zeros(nn)
bin2=np.zeros(nn)

fin=open("pyrand_out.dat","r")

for i in range(n):
    x[i]=float(fin.readline() )
    val=int(x[i]*100000)+1
    if(val<10000):
        bin1[val]+=1
           
fin.close()

"""
fin=open("tcrand_out.dat","r")

for i in range(n):
    x[i]=float(fin.readline() )
    val=int(x[i]*100000)+1
    if(val<10000):
        bin2[val]+=1
#        if(val==510):print(val,x[i])
        
fin.close()
"""

for i in range(n):
    test = int(x[i]*32768.0)
    val=test/32768.0
    val=int(val*100000)+1
    if(val<10000):
        bin2[val]+=1


histout=plt.hist([bin1,bin2],20,range=(0,10)) #nb - use 'list' for multiple histograms  

#plot expected Poisson distribution
a=1.0
for i in range(10):
    prob=nn*(a**i * np.exp(-a)/factorial(i))
    plt.plot(i,prob,'*k')

plt.xlabel('events per bin')
plt.ylabel('number of bins')


    
