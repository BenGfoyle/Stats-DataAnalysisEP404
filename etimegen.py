#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
etimegen - routine to generate sequence of periodic event times with
missing events determined by value of selection threshold

Created on Tue Mar  5 15:35:03 2019
@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

fid=open('etimegen_out.dat','w')

iseed = 1234
freq = 2.0
tmax = 100.0
thresh = 0.4

rnd.seed(iseed)
t = 0

while t < tmax:
    deltat = 1/freq
    t = t + deltat
    x = rnd.random()
    if x < thresh: fid.write('%12.6f\n' % t)

fid.close()
