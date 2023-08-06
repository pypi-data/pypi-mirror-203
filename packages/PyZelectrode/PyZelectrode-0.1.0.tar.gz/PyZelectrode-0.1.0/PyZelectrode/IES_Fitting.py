#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:10:13 2023

@author: aguimera
"""

from PyZelectrode.Helper import CalculateIEScolumns
import numpy as np
from lmfit import minimize
import pandas as pd

def leastsq_errorfunc(params, IESpd, circuit, weight_func):
    Wreq = IESpd.Wreq.values
    Zre = IESpd.Zre.values
    Zim = IESpd.Zim.values
    
    zfit = circuit(params, Wreq)
    re_fit = np.real(zfit)
    im_fit = np.imag(zfit)
    
    error = [(Zre-re_fit)**2, (Zim-im_fit)**2] #sum of squares
    
    #Different Weighing options, see Lasia
    if weight_func == 'modulus':
        weight = [1/((re_fit**2 + im_fit**2)**(1/2)), 1/((re_fit**2 + im_fit**2)**(1/2))]
    elif weight_func == 'proportional':
        weight = [1/(re_fit**2), 1/(im_fit**2)]
    elif weight_func == 'proportional2':
        weight = [1/re_fit, 1/re_fit]
    elif weight_func == 'unity':
        unity_1s = []
        for k in range(len(Zre)):
            unity_1s.append(1) #makes an array of [1]'s, so that the weighing is == 1 * sum of squres.
        weight = [unity_1s, unity_1s]
    else:
        print('weight not defined in leastsq_errorfunc()')
        
    S = np.array(weight) * error #weighted sum of squares 
    return S


def FittingIES(IES, EquivalentCircuit, CircuitParameters, weight_func, FittingFreqRange):
   # find frequnecy index
    FreqIndMin = np.argmin(np.abs(IES.Freq-FittingFreqRange[0]))
    FreqIndMax = np.argmin(np.abs(IES.Freq-FittingFreqRange[1]))
    FInds = np.arange(FreqIndMax, FreqIndMin, 1, dtype=int) 
            
    # Fintting        
    FunctArgs = (IES.iloc[FInds],    # apply the Frequency index 
                 EquivalentCircuit,         #choose model
                 weight_func)

    # Launch minimizer
    fit = minimize(leastsq_errorfunc,
                   CircuitParameters,
                   method='leastsq',
                   args=FunctArgs,
                   nan_policy='omit',
                   max_nfev=10000)
    
    # Calculate IES from fitted parameters
    IESfit = pd.DataFrame(data={'Z': EquivalentCircuit(fit.params, IES.Wreq[FInds]),
                                'Freq': IES.Freq[FInds]})
    CalculateIEScolumns(IESfit)

#        Add column with fitting data
    FitVals = {}                  
    FitVals['IESfit'] = IESfit
    FitVals['Fit'] = fit
    for p in fit.params:
        FitVals[p] = fit.params[p].value
        FitVals[p+'_std'] = fit.params[p].stderr
        # dSel.loc[i, p+'_bnd'] = fit.params[p].bounds
    
    FitVals['FitChi'] = fit.redchi
    FitVals['chisqr'] = fit.chisqr

    return FitVals
