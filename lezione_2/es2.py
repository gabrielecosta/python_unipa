"""
chiedere all'utente la lunghezza dei lati di un rettangolo e poi stampare:
1. l'area del rettangolo
2. il perimetro del rettangolo
3. la lunghezza della diagonale
"""

import math

base = int(input("Inserisci base: "))
altezza = int(input("Inserisci altezza: "))

area = base*altezza
perimetro = (base + altezza)*2

diagonale = math.sqrt(base**2 + altezza**2)

print(f"Area: {area} \nPerimetro: {perimetro}")
print("Diagonale: {:.2f}".format(diagonale))
