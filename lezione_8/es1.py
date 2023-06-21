"""
Scrivere un programma che implementi il cosidetto Crivello di Eratostene.
Scegliere un numero interno n. Il programma deve calcolare tutti i numeri primi fino ad n.
Innanzitutto, inserisce tutti i numeri da 2 ad n all'interno di un set. Poi eliminare tutti i valori
multipli di 2 (eccetto 2); e quindi 4,6,8,10,etc... Cancellare quindi tutti i multipli di 3 (eccetto 3).
E così via fino ad arrivare a rad(n). I numeri restanti sono tutti primi
"""

import math

try:
    n = int(input("Inserisci un valore: "))
except ValueError as err:
    print(err)

primi =  {elem for elem in range(2,n+1)}
print(f"Set appena creato: {primi}")

rad = math.sqrt(n)

index = 2

while index < rad:
    to_discard = {elem for elem in primi if elem%index==0 and elem!=index}
    primi = primi.difference(to_discard)
    index += 1

print(f"Set con numeri primi: {primi}")


