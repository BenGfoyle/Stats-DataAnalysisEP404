#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:27:10 2019

@author: mfc
"""

import numpy as np
import matplotlib.pyplot as plt
plt.ion
from scipy.special import gamma

a=np.linspace(0.1,5.0,1000)
plt.plot(a,gamma(a))
plt.grid()