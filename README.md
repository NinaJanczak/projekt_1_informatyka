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
- Program wykożystuje biblioteki: math, numpy, argparse

## Opis pracy programu:
Aby program dokonał transformacji należy w konsoli odpowiedzieć na zadawane pytania.
```sh
-d
```
Plik z danymi lub cieżka do niego.
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
Jeśli wpiszemy słowo koniec z dowolną wielkocią znaków program zakończy działanie a na konsoli powstanie wydruk.
```sh
Koniec!!
```
Jeżli jednak program ma policzyć następne transformacje należy kliknąć jakikolwiek klawisz na klawiaturz, a następnie od poczatku usupełniać dane.

## Przykładowe transformacje:

## Błędy
