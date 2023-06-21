"""
8. Classi:
Definisci una classe Shape con un metodo area e una classe derivata Rectangle che estende la classe Shape e implementa 
il metodo area per calcolare l'area del rettangolo.
"""

class Shape():
    def __init__(self, num_lati, colore):
        self.num_lati = num_lati
        self.colore = colore
    
    def print_shape(self):
        print(f"Numero lati: {self.num_lati}, Colore: {self.colore}")
    
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, num_lati, colore, base, altezza):
        super().__init__(num_lati, colore)
        self.base = base
        self.altezza = altezza

    def print_lati(self):
        print("Altezza: {0}, Base: {1}".format(self.altezza, self.base))

    def area(self):
        return self.base*self.altezza
   

figura = Rectangle(4, 'Rosso', 5.264, 4.5)
figura.print_lati()
figura.print_shape()
print("Area: {:.2f}".format(figura.area()))