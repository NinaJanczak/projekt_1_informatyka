# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:53:25 2023

@author: ninaj i jansy
"""

def XYZ2BLH(X,Y,Z,a,e2):
    p = np.sqrt(X**2 + Y**2)
    B = np.arctan(Z /( p * (1 - e2)))
    wHile True:
        N = a / np.sqrt(1- e2 * np.sin(B)**2)
        H = (p / np.cos(B)) - N
        Bp = B
        B = np.arctan(Z / (p * (1 - e2 * (N / (N + H)))))
        if np.abs(Bp - B) <( 0.000001/206265):
            break
    L = np.arctan2(Y,X)
    
    B = B * 180 / pi
    L = L * 180 / pi
    return (B,L,H)

def BLH2XYZ(B,L,H,a,e2):
    N = a / np.sqrt(1- e2 * np.sin(B)**2)
    B = B * pi / 180
    L = L * pi / 180
    X = (N + H) * np.cos(B) * np.cos(L)
    Y = (N + H) * np.cos(B) * np.sin(L)
    Z = (N * (1 - e2) + H) * np.sin(B)
    return(X,Y,Z)

def XYZ2NEU(X,Y,Z,a,e2,s,alfa,z):
    p = np.sqrt(X**2 + Y**2)
    B = np.arctan(Z /( p * (1 - e2)))
    while True:
        N = a / np.sqrt(1- e2 * np.sin(B)**2)
        H = (p / np.cos(B)) - N
        Bp = B
        B = np.arctan(Z / (p * (1 - e2 * (N / (N + H)))))
        if np.abs(Bp - B) <( 0.000001/206265):
            break
    L = np.arctan2(Y,X)
    R = np.array([[-np.sin(B)*np.cos(L), -np.sin(L), np.cos(B)*np.cos(L)],
                  [-np.sin(B)*np.sin(L), np.cos(L), np.cos(B)*np.sin(L)],
                  [np.cos(B), 0, np.sin(B)]])
    dneu = np.array([s * np.sin(z) * np.cos(alfa), 
                     s * np.sin(z) * np.sin(alfa), 
                     s * cos(z)])
    return(dneu[0], dneu[1],dneu[2])

def BL2XY2000(B,L,a,e2):
    L0 = 0
    n = 0
    if L > 13.5 * pi / 180 and L < 16.5 * pi / 180:
        L0 = L0 + (15 * pi / 180)
        n = n + 5
    if L > 16.5 * pi / 180 and L < 19.5 * pi / 180: 
        L0 = L0 + (18 * pi / 180)
        n = n + 6
    if L > 19.5 * pi / 180 and L < 22.5 * pi / 180: 
        L0 = L0 + (21 * pi / 180)
        n = n + 7
    if L > 22.5 * pi / 180 and L < 25.5 * pi / 180: 
        L0 = L0 + (24 * pi / 180)
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
    B = B * pi / 180
    L = L * pi / 180
    L0 = 19 * pi / 180
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
