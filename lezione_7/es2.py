"""
Scrivere un programma che dato un file di testo stampi il numero di caratteri,
parole e righe in quel file (esempio dal file2)
"""
import os
print(os.getcwd())
filename = os.getcwd() + '\input2.txt'
print(f"Filename: {filename}")


rows = 0
caratteri = 0
parole = 0

with open(filename, 'r') as f:
    for row in f:
        if row != '':
            rows += 1
        row = row.strip('.,?!)<>;:»«')
        values = row.split()
        parole += len(values)
        for elem in values:
            elem = elem.strip('.,?!)<>;:»«')
            caratteri += len(elem)

print(f"Numero di righe: {rows}")
print(f"Numero di parole: {parole}")
print(f"Numero di caratteri: {caratteri}")