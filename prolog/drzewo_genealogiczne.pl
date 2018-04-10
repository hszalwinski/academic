rodzice(jan,ewa,[adam],[maria]).
rodzice(adam,halina,[norbert],[monika]).
rodzice(piotr,maria,[krzysztof],[]).
ojciec(edward,[],[halina]).
matka(monika,[maciej],[]).

%!  %%%%%%%%%%%%%%%%%%

element(E,[E|_]).
element(E,[_|O]):-element(E,O).
nelement(_,[]).
nelement(E,[G|O]) :- E\==G,nelement(E,O).
czy_wspolny(L1,L2) :- element(G,L1),element(G,L2).
wspolny(G,L1,L2) :- element(G,L1),element(G,L2).

%!   %%%%%%%%%%%%%%%%%%

ojciec2(X,S,C):-rodzice(X,_,S,C) ; ojciec(X,S,C).
matka2(X,S,C):-rodzice(_,X,S,C) ; matka(X,S,C).

rodzic_syna(R,X):-ojciec2(R,S,_),element(X,S).
rodzic_syna(R,X):-matka2(R,S,_),element(X,S).

rodzic_corki(R,X):-ojciec2(R,_,C),element(X,C).
rodzic_corki(R,X):-matka2(R,_,C),element(X,C).

rodzic(R,X):-rodzic_syna(R,X) ; rodzic_corki(R,X).

dziecko(D,R):-rodzic(R,D).
syn(S,R):-rodzic_syna(R,S).
corka(C,R):-rodzic_corki(R,C).

lista_mezczyzn(L):-findall(X, (ojciec2(X,_,_) ; syn(X,_)), L).
mezczyzni(S):-lista_mezczyzn(L), list_to_set(L,S).
mezczyzna(X):-mezczyzni(L), element(X,L).

lista_kobiet(L):-findall(X, (matka2(X,_,_) ; corka(X,_)), L).
kobiety(S):-lista_kobiet(L), list_to_set(L,S).
kobieta(X):-kobiety(L), element(X,L).

lista_rodzenstw(L):-findall((X,Y), (rodzic(R,X),rodzic(R,Y),X\==Y), L).
rodzenstwa(S):-lista_rodzenstw(L), list_to_set(L,S).
rodzenstwo(X,Y):-rodzenstwa(L), element((X,Y),L).

brat(B,X):-rodzenstwo(B,X),mezczyzna(B).
siostra(S,X):-rodzenstwo(S,X),kobieta(S).

potomek(P,X):-rodzic(X,P).
potomek(P,X):-rodzic(X,Y),potomek(P,Y).

przodek(P,X):-rodzic(P,X).
przodek(P,X):-rodzic(Y,X),przodek(P,Y).

dziadek(D,X):-rodzic(Y,X),rodzic(D,Y),mezczyzna(D).
babcia(B,X):-rodzic(Y,X),rodzic(B,Y),kobieta(B).

stryj(S,X):-rodzic(R,X),mezczyzna(R),brat(S,R).
stryjenka(S,X):-rodzic(R,X),mezczyzna(R),siostra(S,R).

wuj(W,X):-rodzic(R,X),kobieta(R),brat(W,R).
ciotka(C,X):-rodzic(R,X),kobieta(R),siostra(C,R).

maz(M,Z):-rodzice(M,Z,_,_).
zona(Z,M):-rodzice(M,Z,_,_).

tesciowa(T,X):-rodzic(T,Z),kobieta(T),zona(Z,X).
tesciowa(T,X):-rodzic(T,M),kobieta(T),maz(M,X).

tesc(T,X):-rodzic(T,Z),mezczyzna(T),zona(Z,X).
tesc(T,X):-rodzic(T,M),mezczyzna(T),maz(M,X).

bratanek(Br,X):-brat(B,X),syn(Br,B).
bratanka(Br,X):-brat(B,X),corka(Br,B).

siostrzeniec(Sc,X):-siostra(S,X),syn(Sc,S).
siostrzenica(Sa,X):-siostra(S,X),corka(Sa,S).

kuzyn(K,X):-syn(K,R), (wuj(R,X) ; ciotka(R,X)).
kuzyn(K,X):-syn(K,R), (stryj(R,X) ; stryjenka(R,X)).

kuzynka(K,X):-corka(K,R), (wuj(R,X) ; ciotka(R,X)).
kuzynka(K,X):-corka(K,R), (stryj(R,X) ; stryjenka(R,X)).

wnuczatko(W,X):-dziadek(X,W) ; babcia(X,W).
wnuk(W,X):-wnuczatko(W,X),mezczyzna(W).
wnuczka(W,X):-wnuczatko(W,X),kobieta(W).

liczba_przodkow(X,Potomek):-findall(Przodek, przodek(Przodek,Potomek), L),
    length(L,X).

czy_matka(brak_danych,M,D):-not(osoba_istnieje_w_bazie(M));
    not(osoba_istnieje_w_bazie(D)).
czy_matka(tak,M,D):-kobieta(M),rodzic(M,D).
czy_matka(nie,M,D):-osoba_istnieje_w_bazie(D),
    kobieta(M),not(rodzic(M,D)).
