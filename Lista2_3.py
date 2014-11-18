import math

class Zespolona:
    rzeczywista = 0
    urojona = 0
    
    def set_rzeczywista (self, liczba):
        self.rzeczywista = liczba
        
    def set_urojona (self, liczba):
        self.urojona = liczba
        
    def get_rzeczywista (self):
        return self.rzeczywista
        
    def get_urojona (self):
        return self.urojona
        
        
    
    def dodaj (self, liczba):
        #print "test"
        wynikDodawania = Zespolona()
        wynikDodawania.set_rzeczywista(self.rzeczywista + liczba.rzeczywista)
        #print wynik.rzeczywista
        wynikDodawania.set_urojona(self.get_urojona() + liczba.get_urojona())
        #print wynik.urojona
        print str(wynikDodawania.get_rzeczywista()) + " + " + str(wynikDodawania.get_urojona()) + " i"
        return wynikDodawania
    
        
    def odejmij (self, liczba):
        #print "test"
        wynikOdejmowania = Zespolona()
        wynikOdejmowania.set_rzeczywista(self.rzeczywista - liczba.rzeczywista)
        #print wynik.rzeczywista
        wynikOdejmowania.set_urojona(self.get_urojona() - liczba.get_urojona())
        #print wynik.urojona
        print str(wynikOdejmowania.get_rzeczywista()) + " + " + str(wynikOdejmowania.get_urojona()) + " i"
        return wynikOdejmowania
    
    def modul (self):
        wynik = math.sqrt(self.get_rzeczywista()**2+self.get_urojona()**2)
        print wynik
        return wynik
    
    def wypisz(self):
        print str(self.get_rzeczywista()) + " + " + str(self.get_urojona()) + "i"
    
    
    
test = Zespolona()
test.rzeczywista = 1
test.urojona =2

test2 = Zespolona()
test2.rzeczywista = 1
test2.urojona =2

test.dodaj(test2)
test.odejmij(test2)
test.modul()
test.wypisz()