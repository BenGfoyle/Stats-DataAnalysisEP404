#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 'n' gaussian deviates, mean 'a', deviation 'b'
Created on Wed Jan  9 15:13:05 2019

@author: mfc
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
plt.ion

def gaussgen(n,a,b):  
    normconst=1.0/np.sqrt(2.0*np.pi)
    total=0
    store=np.zeros(n)
    rnd.seed(1234)
    i=0
    while i in range(n):
        total+=1
        x=12.0*rnd.random() - 6.0
        y=0.4*rnd.random()
        test = normconst*np.exp(-x**2/2.0)
        if(y<test):
            store[i]=x*b+a
            i+=1
        
    return store
    
n=10
a=23.4
b=0.67    
gauss=gaussgen(n,a,b)



