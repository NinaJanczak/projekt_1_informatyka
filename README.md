# Transformacje współrzędnych geodezyjnych 
Program służy do transformowania współrzędnych między różnymi układami.
##### Dostępne warianty transformacji:
- XYZ (geocentryczne) --> BLH (elipsoidalne)
- BLH --> XYZ
- XYZ --> NEUp (topocentryczne)
- BL --> PL2000
- BL --> PL1992
##### Dostępne modele elipsoidy:
- GRS80
- WGS84
- Krasowski

## Minimalne wymagania sprzętowe i programowe:
- Windows 10
- Python 3.10 - zalecana alpikacja spyder (5.4.3)
- Program wykorzystuje biblioteki: math, numpy, argparse

## Opis pracy programu:
Aby program dokonał transformacji należy w konsoli odpowiedzieć na zadawane pytania.
```sh
-d
```
Plik z danymi lub ścieżka do niego.
```sh
-t
```
Wybrana transformacja (XYZ2BLH, BLH2XYZ, XYZ2NEU, BL2XY2000, BL2XY1992)
```sh
-e
```
Wybrany model elipsoidy (WGS84/ GRS80/ KRASOWSKI)

### Przykładowe wywołanie:
```sh
projekt1.py
-d dane_XYZ.txt
-t XYZ2BLH
-e GRS80
```
Po wpisaniu powyższych danych na konsoli pojawi się następujący wydruk:
```sh
Raport został utworzony i zapisany w folderze gdzie znajduje się kod.
Jezeli chcesz zamknąć program wpisz - KONIEC, jesli chcesz kontynuwować napisz cokolwiek: 
```
Jeśli wpiszemy słowo koniec z dowolną wielkością znaków program zakończy działanie a na konsoli powstanie wydruk.
```sh
Koniec!!
```
Jeżli jednak program ma policzyć następne transformacje należy kliknąć jakikolwiek klawisz na klawiaturz, a następnie od poczatku uzupełniać dane.

## Przykładowe transformacje:
BLH2XYZ
Plik z danymi wejściowymi.
```sh
 1 53.19981 17.89264 127
 2 52.88036 32.096429 54
 3 51.78945 22.073928 20
 10 49.54902 19.258147 100
 57 60.149325 16.492767 113
```
Raport zapisany na komputerze użytkownika.
```sh
  Nr_pkt        X[m]            Y[m]            Z[m]      
    1        3636468.320     1174031.426     5073793.342  
    2        3263562.447     2046945.431     5056055.801  
    3        3668314.510     1487603.951     4994752.536  
    10       3912270.357     1366850.136     4828075.090  
    57       3046098.788     901877.305      5498601.368  
```
Wydruk z konsoli:
```sh
Wklej sciezke do pliku txt z danymi: C:/Users/ninaj/Pulpit/Nauka/INF/dane_BLH.txt
Nazwa transformacji:blh2xyz
Model elipsoidy:grs80
Raport został utworzony i zapisany w folderze gdzie znajduje się kod.
Jezeli chcesz zamknąć program wpisz - KONIEC, jesli chcesz kontynuwować napisz cokolwiek: koniec
Koniec!!
```

## Błędy
Jeśli ścieżka do pliku będzie błędna lub nazwa transformacji albo model geoidy(nie uwzgledniając wielkoci znaków) pojawi się następujący komunikat:
```sh
Podano niewłasciwe paramerty programu.
```
Jesli natomiast program będzie miał problem z odczytaniem danych z pliku wejciowego pokaże nam się komentarz:
```sh
Zly format danych w pliku.
```
