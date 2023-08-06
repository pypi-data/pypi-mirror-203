#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:00:18 2022

@author: aguimera
"""

import scipy as sp
import scipy.interpolate
import numpy as np
import pandas as pd

def log_interp1d(xx, yy, kind='linear'):
    logx = np.log10(xx)
    # logy = np.log10(yy)
    lin_interp = sp.interpolate.interp1d(logx, yy, kind=kind)
    # log_interp = lambda zz: np.power(10.0, lin_interp(np.log10(zz)))
    log_interp = lambda zz: lin_interp(np.log10(zz))
    return log_interp

def CalculateIEScolumns(IESin):
    if 'Wreq' not in IESin:
        IESin['Wreq'] = IESin.Freq*np.pi*2    
    if 'Z' not in IESin:    
        IESin['Z'] = np.vectorize(np.complex)(IESin.Zre.values, IESin.Zim.values)
    if 'Zim' not in IESin:
        IESin['Zim'] =  np.imag(IESin.Z)    
    if 'Zre' not in IESin:
        IESin['Zre'] = np.real(IESin.Z)
    if 'Zabs' not in IESin:
        IESin['Zabs'] =  np.abs(IESin.Z)    
    if 'Zpha' not in IESin:
        IESin['Zpha'] = np.angle(IESin.Z, deg=True)
    if 'Y' not in IESin:
        IESin['Y'] = 1/IESin['Z']
    if 'Yre' not in IESin:
        IESin['Yre'] = np.real(IESin.Y)
    if 'Yim' not in IESin:
        IESin['Yim'] = np.imag(IESin.Y)
    if 'Cs' not in IESin:
        IESin['Cs'] = -1/(IESin.Zim*IESin.Wreq)
    if 'Cp' not in IESin:
        IESin['Cp'] = IESin.Yim*IESin.Wreq
    if 'Rs' not in IESin:
        IESin['Rs'] = IESin.Zre
    if 'Rp' not in IESin:
        IESin['Rp'] = 1/IESin.Yre

        
HeadersTranslation = {'  Freq(Hz)': 'Freq',
                      'Ampl': 'Ampl',
                      'Bias': 'Bias',
                      'Time(Sec)': 'Time',
                      "Z'(a)": 'Zre',
                      "Z''(b)": 'Zim',
                      'freq/Hz': 'Freq',
                      'Re(Z)/Ohm': 'Zre',
                      '-Im(Z)/Ohm': 'Zim',
                      '|Z|/Ohm': 'Zabs',
                      'Phase(Z)/deg': 'Zpha',
                      'time/s': 'Time',
                      '<Ewe>/V': 'Bias',
                      '<I>/mA': 'Ibias',
                      'Cs/µF': 'Cs',
                      'Cp/µF': 'Cp',
                      'cycle number': 'Cycle',
       #                'I Range', '|Ewe|/V', '|I|/A', '(Q-Qo)/mA.h', '<Ece>/V', '|Ece|/V',
       # 'Phase(Zce)/deg', '|Zce|/Ohm', 'Re(Zce)/Ohm', '-Im(Zce)/Ohm',
       # 'Phase(Zwe-ce)/deg', '|Zwe-ce|/Ohm', 'Re(Zwe-ce)/Ohm',
       # '-Im(Zwe-ce)/Ohm', 'P/W', 'Re(Y)/Ohm-1', 'Im(Y)/Ohm-1', '|Y|/Ohm-1',
       # 'Phase(Y)/deg', '<I>/mA.1', 'dq/mA.h',
                      
                      }

def extract_solar(FileIn):
    '''
    Extracting data files from Solartron's '.z' format, coloums are renames following correct_text_EIS()
    
    Kristian B. Knudsen (kknu@berkeley.edu || kristianbknudsen@gmail.com)
    '''
    dummy_col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K','L','M','N','O','P']
    init = pd.read_csv(FileIn, encoding='latin1', sep='\t', names=dummy_col)
    ZC = pd.Index(init.A)
    header_loc = ZC.get_loc('  Freq(Hz)')
    
    header_names_raw = pd.read_csv(FileIn, sep='\t', skiprows=header_loc, encoding='latin1') #locates number of skiplines
    header_names = []
    for col in header_names_raw.columns:
        if col in HeadersTranslation:
            header_names.append(HeadersTranslation[col]) #reads coloumn text
        else:
            header_names.append(col) #reads coloumn text
    data = pd.read_csv(FileIn, sep='\t', skiprows=header_loc+2, names=header_names, encoding='latin1')
    # data.update({'im': -data.im})
    data = data.assign(cycle_number = 1.0)
    return data

def extract_mpt(FileIn):
    '''
    Extracting PEIS and GEIS data files from EC-lab '.mpt' format, coloums are renames following correct_text_EIS()
    
    Kristian B. Knudsen (kknu@berkeley.edu || kristianbknudsen@gmail.com)
    '''
    EIS_init = pd.read_csv(FileIn, sep='\t', nrows=1,header=0,names=['err'], encoding='latin1') #findes line that states skiplines
#    EIS_test_header_names = pd.read_csv(path+EIS_name, sep='\t', skiprows=int(EIS_init.err[0][18:20])-1, encoding='latin1') #locates number of skiplines
    EIS_test_header_names = pd.read_csv(FileIn, sep='\t', skiprows=int(EIS_init.err[0][18:-1])-1, encoding='latin1') #locates number of skiplines
    names_EIS = []
    for col in EIS_test_header_names.columns:
        if col in HeadersTranslation:
            names_EIS.append(HeadersTranslation[col]) #reads coloumn text
        else:
            names_EIS.append(col) #reads coloumn text
   
    # return pd.read_csv(path+EIS_name, sep='\t', skiprows=int(EIS_init.err[0][18:20]), names=names_EIS, encoding='latin1')
    data =  pd.read_csv(FileIn, sep='\t',
                       skiprows=int(EIS_init.err[0][18:-1]),
                       names=names_EIS,
                       encoding='latin1',
                       dtype=float,
                       )
    
    data.Zim = -data.Zim

    return data