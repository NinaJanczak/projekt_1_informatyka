# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:53:25 2023

@author: ninaj i jansy
"""

def Np(f,a,e2):
    N = a / np.sqrt(1- e2 * np.sin(f)**2)
    return(N)

def XYZ2BLH(X,Y,Z,a,e2):
    #hirvonen
    p = np.sqrt(X**2 + Y**2)
    #print('p=',p)
    f = np.arctan(Z /( p * (1 - e2)))
    #dms(f)
    while True:
        N = Np(f,a,e2)
        #print('N = ',N)
        h = (p / np.cos(f)) - N
       # print('h = ',h)
        fp = f
        f = np.arctan(Z / (p * (1 - e2 * (N / (N + h)))))
        #dms(f)
        if np.abs(fp - f) <( 0.000001/206265):
            break
    l = np.arctan2(Y,X)
    return (f,l,h)

def BLH2XYZ(f,l,h,a,e2):
    N = Np(f,a,e2)
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

def fl2xygk(fi,lam,lam0,a,e2):
    b2 = (a ** 2) * (1 - e2)
    ep2 = (a ** 2 - b2) / b2
    dl = lam - lam0
    t = tan(fi)
    n2 = ep2 * (cos(fi) ** 2)
    N = Np(fi,a,e2)
    sig = sigma(fi,a,e2)
    xgk = sig + ((dl ** 2 / 2) * N * sin(fi) * cos(fi) * (1 + (((dl ** 2)/12) * (cos(fi) ** 2) * (5 - t **2 + 9 * n2 + 4 * n2 ** 2)) + (((dl ** 4) / 360) * (cos(fi) ** 4 ) * (61 - 58 * (t ** 2) + t ** 4 + 270 * n2 - 330 * n2 * (t ** 2)))))
    ygk = dl * N * cos(fi) * (1 + (((dl ** 2)/6) * (cos(fi) ** 2) * (1 - t ** 2 + n2)) + (((dl ** 4 ) / 120) * (cos(fi) ** 4) * (5 - 18 * t ** 2 + t ** 4 + 14 * n2 - 58 * n2 * t ** 2)))   
    return(xgk,ygk) 

def strefy2000(l):
    lam0 = 0
    n = 0
    if l > dms2rad(13, 30, 0) and l < dms2rad(16, 30, 0):
        lam0 = lam0 + dms2rad(15, 0, 0)
        n = n + 5
    if l > dms2rad(16, 30, 0) and l < dms2rad(19, 30, 0): 
        lam0 = lam0 + dms2rad(18, 0, 0)
        n = n + 6
    if l > dms2rad(19, 30, 0) and l < dms2rad(22, 30, 0): 
        lam0 = lam0 + dms2rad(21, 0, 0)
        n = n + 7
    if l > dms2rad(22, 30, 0) and l < dms2rad(25, 30, 0): 
        lam0 = lam0 + dms2rad(24, 0, 0)
        n = n + 8
    return(lam0,n)

def xy2000(xgk,ygk,n):
    m = 0.999923
    x = xgk * m
    y = ygk * m + n * 1000000 + 500000
    return(x,y)

def xy1992(xgk,ygk):
    m = 0.9993 
    x = xgk * m - 5300000
    y = ygk * m + 500000
    return(x,y)
