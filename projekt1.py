# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:53:25 2023

@author: ninaj i jansy
"""

def XYZ2BLH(X,Y,Z,a,e2):
    #hirvonen
    p = np.sqrt(X**2 + Y**2)
    f = np.arctan(Z /( p * (1 - e2)))
    while True:
        N = a / np.sqrt(1- e2 * np.sin(f)**2)
        h = (p / np.cos(f)) - N
        fp = f
        f = np.arctan(Z / (p * (1 - e2 * (N / (N + h)))))
        if np.abs(fp - f) <( 0.000001/206265):
            break
    l = np.arctan2(Y,X)
    return (f,l,h)

def BLH2XYZ(f,l,h,a,e2):
    N = a / np.sqrt(1- e2 * np.sin(f)**2)
    X = (N + h) * np.cos(f) * np.cos(l)
    Y = (N + h) * np.cos(f) * np.sin(l)
    Z = (N * (1 - e2) + h) * np.sin(f)
    return(X,Y,Z)

def XYZ2NEU(X,Y,Z,a,e2,s,alfa,z):
    p = np.sqrt(X**2 + Y**2)
    f = np.arctan(Z /( p * (1 - e2)))
    while True:
        N = a / np.sqrt(1- e2 * np.sin(f)**2)
        h = (p / np.cos(f)) - N
        fp = f
        f = np.arctan(Z / (p * (1 - e2 * (N / (N + h)))))
        if np.abs(fp - f) <( 0.000001/206265):
            break
    l = np.arctan2(Y,X)
    R = np.array([[-np.sin(f)*np.cos(l), -np.sin(l), np.cos(f)*np.cos(l)],
                  [-np.sin(f)*np.sin(l), np.cos(l), np.cos(f)*np.sin(l)],
                  [np.cos(f), 0, np.sin(f)]])
    dneu = np.array([s * np.sin(z) * np.cos(alfa), 
                     s * np.sin(z) * np.sin(alfa), 
                     s * cos(z)])
    return(dneu[0], dneu[1],dneu[2])

def BL2XY2000(B,L,a,e2):
    L0 = 0
    n = 0
    if L > dms2rad(13, 30, 0) and L < dms2rad(16, 30, 0):
        L0 = L0 + dms2rad(15, 0, 0)
        n = n + 5
    if L > dms2rad(16, 30, 0) and L < dms2rad(19, 30, 0): 
        L0 = L0 + dms2rad(18, 0, 0)
        n = n + 6
    if L > dms2rad(19, 30, 0) and L < dms2rad(22, 30, 0): 
        L0 = L0 + dms2rad(21, 0, 0)
        n = n + 7
    if L > dms2rad(22, 30, 0) and L < dms2rad(25, 30, 0): 
        L0 = L0 + dms2rad(24, 0, 0)
        n = n + 8
        
    b2 = (a ** 2) * (1 - e2)
    ep2 = (a ** 2 - b2) / b2
    dL = L - L0
    t = np.tan(B)
    n2 = ep2 * (np.cos(B) ** 2)
    N = a / np.sqrt(1- e2 * np.sin(B)**2)
    
    A0 = 1 - (e2 / 4) - ((3 * e2 ** 2) / 64) - ((5 * e2 ** 3) / 256)
    A2 = (3 / 8) * (e2 + (e2 ** 2) / 4 + (15 * e2 ** 3) / 128)
    A4 = (15 / 256) * (e2 ** 2 + (3 * e2 ** 3) / 4)
    A6 = (35 * e2 ** 3) / 3072
    sig = a * ((A0 * B) - (A2 * np.sin(2 * B)) + (A4 * np.sin(4 * B)) - (A6 * np.sin(6 * B)))
    
    Xgk = sig + ((dL ** 2 / 2) * N * np.sin(B) * np.cos(B) * (1 + (((dL ** 2)/12) * (np.cos(B) ** 2) * (5 - t **2 + 9 * n2 + 4 * n2 ** 2)) + (((dL ** 4) / 360) * (np.cos(B) ** 4 ) * (61 - 58 * (t ** 2) + t ** 4 + 270 * n2 - 330 * n2 * (t ** 2)))))
    Ygk = dL * N * np.cos(B) * (1 + (((dL ** 2)/6) * (np.cos(B) ** 2) * (1 - t ** 2 + n2)) + (((dL ** 4 ) / 120) * (np.cos(B) ** 4) * (5 - 18 * t ** 2 + t ** 4 + 14 * n2 - 58 * n2 * t ** 2)))   
    
    X = Xgk * 0.999923
    Y = Ygk * 0.999923 + n * 1000000 + 500000
    
    return(X,Y) 


def BL2XY1992(B,L,a,e2):
    L0 = dms2rad(19,0,0)
    b2 = (a ** 2) * (1 - e2)
    ep2 = (a ** 2 - b2) / b2
    dL = L - L0
    t = np.tan(B)
    n2 = ep2 * (np.cos(B) ** 2)
    N = a / np.sqrt(1- e2 * np.sin(B)**2)
    
    A0 = 1 - (e2 / 4) - ((3 * e2 ** 2) / 64) - ((5 * e2 ** 3) / 256)
    A2 = (3 / 8) * (e2 + (e2 ** 2) / 4 + (15 * e2 ** 3) / 128)
    A4 = (15 / 256) * (e2 ** 2 + (3 * e2 ** 3) / 4)
    A6 = (35 * e2 ** 3) / 3072
    sig = a * ((A0 * B) - (A2 * np.sin(2 * B)) + (A4 * np.sin(4 * B)) - (A6 * np.sin(6 * B)))
    
    Xgk = sig + ((dL ** 2 / 2) * N * np.sin(B) * np.cos(B) * (1 + (((dL ** 2)/12) * (np.cos(B) ** 2) * (5 - t **2 + 9 * n2 + 4 * n2 ** 2)) + (((dL ** 4) / 360) * (np.cos(B) ** 4 ) * (61 - 58 * (t ** 2) + t ** 4 + 270 * n2 - 330 * n2 * (t ** 2)))))
    Ygk = dL * N * np.cos(B) * (1 + (((dL ** 2)/6) * (np.cos(B) ** 2) * (1 - t ** 2 + n2)) + (((dL ** 4 ) / 120) * (np.cos(B) ** 4) * (5 - 18 * t ** 2 + t ** 4 + 14 * n2 - 58 * n2 * t ** 2)))   
    
    X = Xgk * 0.9993 - 5300000
    Y = Ygk * 0.9993 + 500000
    return(X,Y) 
