"""
Scrivere un programma che legga tre numeri e stampi:
- crescenti se sono in ordine strettamente crescente
- decrescenti se sono in ordine strettamente decrescente
- nessuna delle due altrimenti
"""

x = int(input("Inserisci numero: "))
y = int(input("Inserisci numero: "))
z = int(input("Inserisci numero: "))

if x>y and y>z:
    print("Strettamente decrescenti")
elif x<y and y<z:
    print("Strettamente crescenti")
else:
    print("Nessuna corrispondenza")
