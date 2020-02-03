#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
randgen: Generate file of random numbers in range [0, 1)
or fill an array with random numbers
Created on Tue Jan  8 17:16:54 2019

@author: mfc
"""

import random as rnd
import numpy as np

fout=open("pyrand_out.dat","w")
n=100000
rnd.seed(12345)
for i in range(n):
    a=rnd.random()
    fout.write("%12.10f \n" % a)
    
fout.close()


#fill array 'b' with random numbers [0,1)
np.random.seed(45678)
b=np.random.rand(n)





