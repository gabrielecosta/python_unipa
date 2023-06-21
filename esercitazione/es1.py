"""
1. Manipolazione di stringhe in input:
Scrivi un programma che chieda all'utente di inserire una frase e restituisca il numero di parole presenti 
nella frase.
Variante: leggere da un file
"""
import os
filename = os.getcwd() + 'input_1.txt'
stringa = input("Inserisci stringa: ")
punteggiatura = '.,;:-_<>!"\''
with open(filename, 'w') as f:
    print(stringa, file=f)
stringa = stringa.strip(punteggiatura)
words = stringa.split()
for elem in words:
    elem = elem.strip(punteggiatura)
print(f"Numero di parole presenti: {len(words)}")

print("Lettura dal file input_1.txt: ")
count = 0
with open(filename, 'r') as f:
    for riga in f:
        riga = riga.strip(punteggiatura)
        words = riga.split()
        count += len(words)
print(f"Numero di parole: {count}")