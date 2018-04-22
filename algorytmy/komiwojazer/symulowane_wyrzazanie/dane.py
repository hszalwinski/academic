import numpy as np

from collections import namedtuple

Punkt = namedtuple('Punkt', ['x', 'y'])  # x(int), y(int)
Cykl = namedtuple('Cykl', ['przejscia', 'koszt'])  # przejscia(lista) np. [0, 3, 1, 2, 0], koszt(float)


def licz_odleglosc(x1, y1, x2, y2):
    return np.sqrt(np.power((x2 - x1), 2) + np.power((y2 - y1), 2))


def licz_odleglosci_miedzy_miastami(miasta, ilosc_miast):
    odleglosci = []
    for j in np.arange(0, ilosc_miast, 1):
        odleglosci.append([])
        for k in np.arange(0, ilosc_miast, 1):
            odleglosc = licz_odleglosc(miasta[j].x, miasta[j].y, miasta[k].x, miasta[k].y)
            odleglosci[j].append(odleglosc)

    return np.array(odleglosci)


# Przynajmniej 3 miasta, zeby byl sens uruchamiac program

# punkty na kwadracie, min droga = 400
# miasta = [
#     Punkt(55, 0),
#     Punkt(100, 0),
#     Punkt(100, 50),
#     Punkt(50, 100),
#     Punkt(5, 100),
#     Punkt(0, 100),
#     Punkt(0, 50),
#     Punkt(100, 25),
#     Punkt(0, 0),
#     Punkt(100, 100),
#     Punkt(20, 0),
#     Punkt(25, 100)
# ]

# punkty losowo, przewidywana min droga to ok. 430-500
miasta = [
    Punkt(1, 2),
    Punkt(5, 50),
    Punkt(40, 99),
    Punkt(99, 89),
    Punkt(54, 22),
    Punkt(87, 98),
    Punkt(24, 13),
    Punkt(7, 99),
    Punkt(34, 56),
    Punkt(77, 48),
    Punkt(22, 4),
    Punkt(25, 35),
    Punkt(5, 14),
    Punkt(48, 78),
    Punkt(79, 3),
    Punkt(88, 25),
    Punkt(40, 15),
    Punkt(55, 55),
    Punkt(10, 67),
    Punkt(90, 87)
]

ilosc_miast = len(miasta)
dlugosc_cyklu = ilosc_miast + 1

odleglosci = licz_odleglosci_miedzy_miastami(miasta, ilosc_miast)
# Przy 3 miastach o odleglosciach 3, 4, 5:
#   odleglosci[0] = [0, 3, 4]
#   odleglosci[1] = [3, 0, 5]
#   odleglosci[2] = [4, 5, 0]

# Wspolczynniki do funkcji obliczającej temperaturę
a = 100
b = 10
