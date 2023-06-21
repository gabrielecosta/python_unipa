"""
Scrivere un programma che legga 3 numeri e stampi "tutti uguali"
se i loro valori sono gli stessi, "tutti differenti" se sono tutti diversi,
"nessuna delle due" altrimenti
"""

x = int(input("Inserisci numero: "))
y = int(input("Inserisci numero: "))
z = int(input("Inserisci numero: "))

if x==y and x==z:
    print("Tutti uguali")
elif x==y or x==z or y==z:
    print("Due valori uguali")
else:
    print("Tutti differenti")