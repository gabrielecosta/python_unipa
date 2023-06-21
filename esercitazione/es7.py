"""
7. Dizionari:
Scrivi un programma che prenda in input una lista di parole e restituisca un dizionario in cui le parole sono 
le chiavi e la loro lunghezza è il valore corrispondente.
"""

stringa = input("Inserisci stringa in input: ")
punteggiatura = ",.:;!"
stringa = stringa.strip(punteggiatura)
stringa_new = stringa.split()
insieme = set()
for word in stringa_new:
    word_new = word.strip(punteggiatura)
    insieme.add(word_new)

dizionario = {}
for parola in insieme:
    count = 0
    for word in stringa_new:
        word = word.strip(punteggiatura)
        if parola == word:
            count += 1
    dizionario[parola] = count

for (key,value) in dizionario.items():
    print(f"Parola: {key}, Conteggio: {value}")
