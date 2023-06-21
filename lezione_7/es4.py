"""
Scrivere un programma che chieda all'utente di inserire dei dati
dopodiche crea un file rinonimato dati.txt
"""

import os
filename = os.getcwd() + '/dati.txt'

with open(filename, 'w') as f:
    nome = input("inserisci nome: ")
    cognome = input("inserisci cognome: ")
    try:
        eta = int(input("inserisci eta: "))
    except ValueError as err:
        print(err)
    if eta > 17:
        value = 'maggiorenne'
    else:
        value = 'minorenne'
    print(f"Ciao {nome} {cognome}. Dai dati inseriti sei {value}", file=f)