class Komputer: 
    def __init__ (self, nrSeryjny):
        self.__nrSeryjny = nrSeryjny    
    def pracuj(self): 
        print "Pracuje!" 
    def get_nrSeryjny(self):
        return self.__nrSeryjny
    def set_nrSeryjny(self, nrSeryjny):
        self.__nrSeryjny = nrSeryjny
 
class Monitor: 
    def __init__ (self, rozdzielczosc):
        self.rozdzielczosc = rozdzielczosc
    def wyswietl(self): 
        print "Wyswietlam z rozdzielczoscia " + str (self.rozdzielczosc) + "px" 
    def get_rozdzielczosc(self):
        return self.__rozdzielczosc
    def set_nrSeryjny(self, rozdzielczosc):
        self.__rozdzielczosc = rozdzielczosc
        
class Laptop(Komputer,Monitor): 
    def __init__ (self, waga, nrSeryjny, rozdzielczosc):
        self.waga = waga
        self.rozdzielczosc = rozdzielczosc
        self.nrSeryjny = nrSeryjny
    def powiedzCos(self):
        print "Jestem laptopem, moja waga to " + str(self.waga) + " moj nr seryjny to " + str(self.nrSeryjny) + " a moja rozdzielczosc to " + str(self.rozdzielczosc) +" px."
    def get_waga(self):
        return self.__waga
    def set_nrSeryjny(self, waga):
        self.__waga = waga
 
class Tablet(Laptop): 
    def __init__ (self, waga, nrSeryjny, rozdzielczosc, system):
        self.waga = waga
        self.rozdzielczosc = rozdzielczosc
        self.nrSeryjny = nrSeryjny
        self.system = system
    def dotknij(self): 
        print "Jestem dotykowy! A moj system to " + self.system
    def get_system(self):
        return self.__system
    def set_nrSeryjny(self, system):
        self.__system = system
        
         
asus = Laptop(2, 15224, 2000) 
asus.pracuj() 
asus.wyswietl()
asus.powiedzCos()
print " "

ipad = Tablet(0.5, 15224, 1000, 'iOS' ) 
ipad.pracuj() 
ipad.wyswietl()
ipad.dotknij()
