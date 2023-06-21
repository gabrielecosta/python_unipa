"""
9. Polimorfismo:
Definisci una classe Shape con un metodo area e una classe derivata Circle che estende la classe Shape e implementa il 
metodo area per calcolare l'area del cerchio.
"""

from es8 import Shape
from math import pi

class Circle(Shape):
    def __init__(self, num_lati, colore, raggio):
        super().__init__(num_lati, colore)
        self.raggio = raggio

    def area(self):
        return pi * self.raggio**2
    

circle = Circle(1, 'blu', 3.5)
circle.print_shape()

print("Area: {:.2f}".format(circle.area()))

