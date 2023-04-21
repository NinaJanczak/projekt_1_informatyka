# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:53:25 2023

@author: ninaj i jansy
"""

import numpy as np
from math import *
from argparse import ArgumentParser


class TransformacjaWspolrzednych:
    def __init__(self):
        self.elipsoidy = {
            'GRS80': {'a': 6378137, 'e2': 0.00669438002290},
            'WGS84': {'a': 6378137, 'e2': 0.00669437999014},
            'Krasowski': {'a': 6378245, 'e2': 0.00669342162297}
        }

    def Odczyt_pliku(self,plik_txt):
        with open(plik_txt,'r') as plik:
            linie = plik.readlines()
            dane = []
            for a in linie:
                a = a.split()
                b = [a[0]]
                a = [b.append(float(i)) for i in a[1:]]

                dane.append(b)
        return dane
    
    def XYZ2BLH(self,plik_txt,elipsoida):
        a = self.elipsoidy[elipsoida]['a']
        e2 = self.elipsoidy[elipsoida]['e2']
        dane_wej = self.Odczyt_pliku(plik_txt)
        dane_wyj = []
        for i in dane_wej:
            Nr_pkt,X,Y,Z = i
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
            
            B = B * 180 / pi
            L = L * 180 / pi
            dane_wyj.append([Nr_pkt,B,L,H])
        with open('raport_XYZ2BLH.txt', 'w') as plik:
            plik.write('{:^10s} {:^15s} {:^15s} {:^15s}\n'.format('Nr_pkt','B[°]','L[°]','H[m]'))
            for a in dane_wyj:
                plik.write('{:^10} {:^15.8f} {:^15.8f} {:^15.3f}\n'.format(a[0], a[1], a[2], a[3]))
        return (dane_wyj)
    
    def BLH2XYZ(self,plik_txt,elipsoida):
        a = self.elipsoidy[elipsoida]['a']
        e2 = self.elipsoidy[elipsoida]['e2']
        dane_wej = self.Odczyt_pliku(plik_txt)
        dane_wyj = []
        for i in dane_wej:
            Nr_pkt,B,L,H = i
            N = a / np.sqrt(1- e2 * np.sin(B)**2)
            B = B * pi / 180
            L = L * pi / 180
            X = (N + H) * np.cos(B) * np.cos(L)
            Y = (N + H) * np.cos(B) * np.sin(L)
            Z = (N * (1 - e2) + H) * np.sin(B)
            dane_wyj.append([Nr_pkt,X,Y,Z])
        with open('raport_BLH2XYZ.txt', 'w') as plik:
            plik.write('{:^10s} {:^15s} {:^15s} {:^15s}\n'.format('Nr_pkt','X[m]','Y[m]','Z[m]'))
            for a in dane_wyj:
                plik.write('{:^10} {:^15.3f} {:^15.3f} {:^15.3f}\n'.format(a[0], a[1], a[2], a[3]))
        return(dane_wyj)
    
    def XYZ2NEU(self,plik_txt,elipsoida):
        a = self.elipsoidy[elipsoida]['a']
        e2 = self.elipsoidy[elipsoida]['e2']
        dane_wej = self.Odczyt_pliku(plik_txt)
        dane_wyj = []
        for i in dane_wej:
            Nr_pkt,X,Y,Z,s,alfa,z = i
            alfa = alfa * pi / 180
            z = z * pi / 180
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
            dane_wyj.append([Nr_pkt,dneu[0], dneu[1],dneu[2]])
        with open('raport_XYZ2NEU.txt', 'w') as plik:
            plik.write('{:^10s} {:^15s} {:^15s} {:^15s}\n'.format('Nr_pkt','northing','easting','up'))
            for a in dane_wyj:
                plik.write('{:^10} {:^15.3f} {:^15.3f} {:^15.3f}\n'.format(a[0], a[1], a[2], a[3]))
        return(dane_wyj)
    
    def BL2XY2000(self,plik_txt,elipsoida):
        a = self.elipsoidy[elipsoida]['a']
        e2 = self.elipsoidy[elipsoida]['e2']
        dane_wej = self.Odczyt_pliku(plik_txt)
        dane_wyj = []
        for i in dane_wej:
            Nr_pkt,B,L = i
            B = B * pi / 180
            L = L * pi / 180
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
            dane_wyj.append([Nr_pkt,X,Y])
        with open('raport_BL2XY2000.txt', 'w') as plik:
            plik.write('{:^10s} {:^15s} {:^15s}\n'.format('Nr_pkt','X[m]','Y[m]'))
            for a in dane_wyj:
                plik.write('{:^10} {:^15.3f} {:^15.3f}\n'.format(a[0], a[1], a[2]))
        return(dane_wyj) 
    
    def BL2XY1992(self,plik_txt,elipsoida):
        a = self.elipsoidy[elipsoida]['a']
        e2 = self.elipsoidy[elipsoida]['e2']
        dane_wej = self.Odczyt_pliku(plik_txt)
        dane_wyj = []
        for i in dane_wej:
            Nr_pkt,B,L = i
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
            dane_wyj.append([Nr_pkt,X,Y])
        with open('raport_BL2XY1992.txt', 'w') as plik:
            plik.write('{:^10s} {:^18s} {:^18s}\n'.format('Nr_pkt','X[m]','Y[m]'))
            for a in dane_wyj:
                plik.write('{:^10} {:^15.3f} {:^15.3f}\n'.format(a[0], a[1], a[2]))
        return(dane_wyj) 

if __name__ == '__main__':
    
    parser = ArgumentParser()

    parser.add_argument('-d', type=str, help='Plik znajduje się w tym samym folderze - podaj jego nazwę wraz z rozszerzeniem. Plik znajduje się w innym miejscu - podaj ścieżkę.')
    parser.add_argument('-t', type=str, help='Przyjmuje nazwe wybranej transformacji (XYZ2BLH, BLH2XYZ, XYZ2NEU, BL2XY2000, BL2XY1992)')
    parser.add_argument('-e', type=str, help='Przyjmuje model elipsoidy (WGS84/ GRS80/ KRASOWSKI)')
    
    args = parser.parse_args()
    
    transformacje = {'XYZ2BLH':'XYZ2BLH', 'BLH2XYZ':'BLH2XYZ', 'XYZ2NEU':'XYZ2NEU', 'BL2XY2000':'BL2XY2000', 'BL2XY1992':'BL2XY1992'}
    
    koniec = ""
    try:
        while koniec != "KONIEC":
            if args.d==None:
                args.d = input(str('Wklej sciezke do pliku txt z danymi: '))
            if args.t==None:
                args.t = input(str('Nazwa transformacji:')).upper()
            if args.e==None:
                args.e = input(str('Model elipsoidy:')).upper()
            obiekt = TransformacjaWspolrzednych()
            transf = transformacje[args.t]
            if transf == 'XYZ2BLH':
                dane_wyj = obiekt.XYZ2BLH(args.d, args.e) 
            if transf == 'BLH2XYZ':
                dane_wyj = obiekt.BLH2XYZ(args.d, args.e)
            if transf == 'XYZ2NEU':
                dane_wyj = obiekt.XYZ2NEU(args.d, args.e)
            if transf == 'BL2XY2000':
                dane_wyj = obiekt.BL2XY2000(args.d, args.e)
            if transf == 'BL2XY1992':
                dane_wyj = obiekt.BL2XY1992(args.d, args.e)
                  
            print('Raport został utworzony i zapisany w folderze gdzie znajduje się kod.')
                
            koniec = input(str("Jezeli chcesz zamknąć program wpisz - KONIEC, jesli chcesz kontynuowac napisz cokolwiek: ")).upper()
            args.e = None
            args.d= None
            args.t= None
    except FileNotFoundError:
        print('Nie ma takiego pliku.')
    except KeyError:
        print('Podano niewlasciwe paramerty programu.')
    except IndexError:
        print('Zly format danych w pliku.')
    except ValueError:
        print('Zly format danych w pliku.')
    finally:
        print('Koniec!!')
        