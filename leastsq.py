#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leastsq: linear least squares fitting (based on 'fit' from Press et al.)
set 'mwt' to zero if uncertainties in y values not available
set 'mwt' to one if errors in y are available (can be unequal)
Created on Fri Jan 11 14:45:46 2019

@author: mfc
"""

import numpy as np; sqrt=np.sqrt
from scipy.special import gammainc

def chiprob(chival,dof):
#convert chi-squared value to probability - uses incomplete gamma function
    x = chival/2.0
    a = dof/2.0
    p = gammainc(a, x)    #args were (x, a) in Matlab 
    prob = 1.0-p
    return prob

def fit(x,y,ndata,sig,mwt):

    sx = 0
    sy = 0
    st2 = 0
    b = 0
    sxoss = 0
    if (mwt == 1):
        ss = 0                                 #accumulate sums
        for i in range(ndata):
            wt = 1/(sig[i]**2)                 #with weights          
            ss = ss + wt
            sx = sx + x[i]*wt
            sy = sy + y[i]*wt
    
    if (mwt == 0):
        for i in range(ndata):                         #without weights
            sx = sx + x[i]
            sy = sy + y[i]
        ss = ndata
    
    sxoss = sx/ss
    
    if (mwt == 1):
        for i in range(ndata):                         #using sigma_y values
            t = (x[i] - sxoss)/sig[i]
            st2 = st2 + t**2
            b = b + (t*y[i])/sig[i]
    
    if (mwt == 0):                                 #not using sigma_y values
        for i in range(ndata):
            t = x[i] - sxoss
            st2 = st2 + t**2
            b = b + t*y[i]
    
    b = b/st2
    a = (sy - sx*b)/ss
    siga = sqrt((1 + sx**2/(ss*st2))/ss)
    sigb = sqrt(1/st2)
    
    chi2 = 0
    
    if (mwt == 0):                                      #calculate chi-squared
        for i in range(ndata):
            chi2 = chi2 + (y[i] - a - b*x[i])**2    #For unweighted data 
            q = 1                                  #evaluate typical sig 
            sigdat = sqrt((chi2)/(ndata-2))        #using chi1, and adjust 
                                                    #the standard deviations
        siga = siga*sigdat                    
        sigb = sigb*sigdat
       
    if (mwt == 1):
        for i in range(ndata):
            chi2 = chi2 + ((y[i] - a - b*x[i])/sig[i])**2
        q = chiprob(chi2,(ndata-2))
    
    return  (a,b,siga,sigb,chi2,q)

            
x=[-2.0, 0.0, 2.0, 4.0]
y=[2.1, 2.4, 2.5, 3.5]
sig=[0.2, 0.2, 0.5, 0.1]
ndata=4

for mwt in range(2):
    a,b,siga,sigb,chi2,q =   fit(x,y,ndata,sig,mwt)
    
    if (mwt == 0):
        print('\nIgnoring Standard Deviations \
              \na = %g\nb = %g\nsiga = %g\nsigb = %g\nchi-squared = %g\n \
              goodness-of-fit (q) = %g' % (a,b,siga,sigb,chi2,q))
        
    if (mwt == 1):
        print('\nIncluding Standard Deviations \
              \na = %g\nb = %g\nsiga = %g\nsigb = %g\nchi-squared = %g\n \
              goodness-of-fit (q) = %g' % (a,b,siga,sigb,chi2,q))
        
