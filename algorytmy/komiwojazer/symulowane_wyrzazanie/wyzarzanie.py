import numpy as np

from random import random
from algorytmy.komiwojazer.symulowane_wyrzazanie.funkcje import stworz_cykl_poczatkowy, stworz_sasiedni_cykl, \
    licz_temperature, licz_prawdopodobienstwo
from matplotlib import pyplot as plt

ilosc_iteracji = 100000
cykl_poczatkowy = stworz_cykl_poczatkowy()
print('Cykl poczatkowy: ' + str(cykl_poczatkowy.przejscia))
print('Poczatkowy koszt: ' + str(cykl_poczatkowy.koszt))

cykl_aktualny = cykl_poczatkowy
cykl_najlepszy = cykl_aktualny

min_koszty = [cykl_poczatkowy.koszt]
numery_iteracji = [0]

for k in np.arange(1, ilosc_iteracji + 1, 1):
    cykl_sasiedni = stworz_sasiedni_cykl(cykl_aktualny)

    if cykl_sasiedni.koszt < cykl_aktualny.koszt:
        cykl_aktualny = cykl_sasiedni
    elif licz_prawdopodobienstwo(cykl_aktualny.koszt, cykl_sasiedni.koszt, T=licz_temperature(k)) > random():
        cykl_aktualny = cykl_sasiedni

    if cykl_aktualny.koszt < cykl_najlepszy.koszt:
        cykl_najlepszy = cykl_aktualny
        min_koszty.append(cykl_najlepszy.koszt)
        numery_iteracji.append(k)
        print('Nowy najlepszy cykl: ' + str(cykl_najlepszy.przejscia))
        print('Koszt najlepszego cyklu: ' + str(cykl_najlepszy.koszt))

print('Dla punktow liczonych od 1:')
przejscia = np.array(cykl_najlepszy.przejscia) + 1
przejscia = list(przejscia)
print('Najlepszy cykl: ' + str(przejscia))
print('Koszt najlepszego cyklu: ' + str(cykl_najlepszy.koszt))

plt.plot(numery_iteracji, min_koszty, 'blue')
plt.xlabel('Iteracja')
plt.ylabel('Aktualny najmniejszy koszt')
plt.title('Postep algorytmu w czasie')
plt.show()
