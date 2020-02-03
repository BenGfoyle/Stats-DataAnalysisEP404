#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monte Carlo integration
Created on Wed Jan  9 15:13:05 2019

@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

n=10000
total=0
success=0
area=0

rnd.seed(1234)

for i in range(n):
    total+=1
    x=np.pi*rnd.random()
    y=1.2*rnd.random()
    if(y<np.sin(x)):
        success+=1
        plt.plot(x,y,'ok')
    else:
        plt.plot(x,y,'+k')
    #plt.pause(0.00001)

area=1.2*np.pi*(success/total)
print(area)



