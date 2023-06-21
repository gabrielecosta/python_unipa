"""
4. File:
Scrivi un programma che legga un file di testo chiamato "input.txt" e stampi il contenuto del file.
"""

import os
filename = os.getcwd() + '\esercizi.txt'
with open(filename, 'r') as f:
    for riga in f:
        print(riga.strip())