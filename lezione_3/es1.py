"""
Scrivere un programma che legga un valore in virgola mobile
e stampi se si tratti di un valore positivo o negativo
"""

x = float(input("Inserisci valore in virgola mobile: "))
if x>0:
    print("Valore positivo")
elif x<0:
    print("Valore negativo")
else:
    print("Valore nullo")