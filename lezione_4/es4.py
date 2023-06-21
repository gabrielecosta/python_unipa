"""
I numeri di Fibonacci sono definiti dalla sequenza:
f1 = 1
f2 = 1
fn = f(n-1) + f(n-2)
Riformulare il problema come:
fold1 = 1
fold2 = 1
fnew = fold1 + fold2
Dopo di che, scartare fold2, che non è più necessario, e impostare fold2 a fold1,
fold1 a fnew.
Implementare un programma che chieda all'utente un numero n e stampi l'n esimo
numero di Fibonacci secondo questo algoritmo
"""

import sys

n = input("Inserisci numero di Fibonacci: ")

if n.isnumeric() == False:
    sys.exit("Errore!")

n = int(n)
fold1 = 1
fold2 = 1

for i in range(3, n+1, 1):
    fnew = fold1 + fold2
    fold2 = fold1
    fold1 = fnew

print(f"Numero di fibonacci: {fnew}")
