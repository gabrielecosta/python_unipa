"""
Scrivere un programma che legga una parola e la stampi in ordine inverso.
Per esempio, se l'utente fornisce l'input "Harry" il programma stamperà
"yrraH"
"""

stringa = input("Inserisci stringa di ingresso: ")

size = len(stringa)

for i in range(size-1, -1, -1):
    print(stringa[i], end='')