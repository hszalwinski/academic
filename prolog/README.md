# Drzewo genealogiczne

## Zadanie

Opisać w prologu relacje rodzinne dla następujcej bazy faktów:

```
rodzice(jan,ewa,[adam],[maria]).
rodzice(adam,halina,[norbert],[monika]).
rodzice(piotr,maria,[krzysztof]).
ojciec(edward,[],[halina]).
matka(monika,[maciej],[]).
```
gdzie:
```
rodzice(imię ojca,imię matki,[imiona synów],[imiona córek]).
ojciec(imię ojca,[imiona synów],[imiona córek]).
matka(imię matki,[imiona synów],[imiona córek]).
```

Przykładowe odpowiedzi programu:
```
kuzyn(krzysztof,norbert)  -> yes
dziadek(edward,monika)    -> yes
zona(halina,adam)         -> yes
potomek(maciej,jan)       -> yes
krewni(maciej,krzysztof)  -> yes
dziadek(jan,X)            -> X=’monika’,X=’norbert’,X=’krzysztof’

liczba_przodkow(X,monika)    -> X=5   

czy_matka(Odp,halina,monika)   -> Odp=‘tak’
czy_matka(Odp,halina,maciej)   -> Odp=‘nie’
czy_matka(Odp,halina,edward)   -> Odp=‘nie’
czy_matka(Odp,halina,piotr)    -> Odp=‘brak_danych
```
