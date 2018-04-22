import numpy as np

from random import randint
from copy import deepcopy

from algorytmy.komiwojazer.symulowane_wyrzazanie.dane import Cykl, ilosc_miast, dlugosc_cyklu, odleglosci, a, b


def stworz_cykl_poczatkowy():
    przejscia = [0]
    for i in np.arange(1, ilosc_miast, 1):
        przejscia.append(i)
    przejscia.append(0)

    cykl = Cykl(przejscia=przejscia, koszt=oblicz_koszt_cyklu(przejscia))

    return cykl


def oblicz_koszt_cyklu(przejscia):
    koszt_cyklu = 0

    for i in np.arange(0, dlugosc_cyklu - 1, 1):
        punkt1 = przejscia[i]
        punkt2 = przejscia[i + 1]
        koszt_przejscia = odleglosci[punkt1][punkt2]
        koszt_cyklu += koszt_przejscia

    return koszt_cyklu


def losuj_indeksy_zmiany_wierzcholkow():
    # przykladowy cykl = [2, 4, 1, 3, 0, 2], jego dlugosc = ilosc elementow w tabeli = 6
    # indeksy w tabeli    0, 1, 2, 3, 4, 5
    # indeksy stale - poczatkowy i koncowy = [0, dlugosc_cyklu - 1]

    indeks1 = randint(1, dlugosc_cyklu - 2)
    indeks2 = randint(1, dlugosc_cyklu - 2)
    if indeks1 == indeks2:
        indeks1, indeks2 = losuj_indeksy_zmiany_wierzcholkow()

    return indeks1, indeks2


def stworz_sasiedni_cykl(cykl):
    indeks1, indeks2 = losuj_indeksy_zmiany_wierzcholkow()

    przejscia = deepcopy(cykl.przejscia)
    przejscia[indeks1], przejscia[indeks2] = przejscia[indeks2], przejscia[indeks1]

    cykl_sasiedni = Cykl(przejscia=przejscia, koszt=oblicz_koszt_cyklu(przejscia))

    return cykl_sasiedni


def licz_temperature(k):
    T = a / np.log10(k + b)

    return T


def licz_prawdopodobienstwo(koszt_aktualnego, koszt_sasiedniego, T):
    wykladnik = -1 * (koszt_sasiedniego - koszt_aktualnego) / T
    prawdopodobienstwo = np.power(np.e, wykladnik)

    return prawdopodobienstwo
