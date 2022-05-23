import ast

liczba_egzemplarzy=int(input())
ksiazki={}

class Ksiazka():
    def __init__(self, tytul, autor, rokWydania):
        self.tytul=tytul
        self.autor=autor
        self.rokWydania=rokWydania
        self.ilosc=1
    def __repr__(self):
        return "'" + self.autor + "', " + str(self.ilosc)

    
for i in range (liczba_egzemplarzy):
    dane_ksiazki=eval(input())
    tytul=dane_ksiazki[0]
    autor=dane_ksiazki[1]
    rokWydania=dane_ksiazki[2]
    
    if tytul in ksiazki.keys():
        ksiazki[tytul].ilosc = ksiazki[tytul].ilosc+1
    else:
        ksiazki[tytul]=Ksiazka(tytul,autor,rokWydania)

posortowane_ksiazki=sorted(ksiazki.items())

for ksiazka in posortowane_ksiazki:
    print(ksiazka)


