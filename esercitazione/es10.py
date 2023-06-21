"""
10. Gestione delle eccezioni:
Scrivi un programma che prenda in input due numeri e restituisca il risultato della divisione tra i due numeri. 
Gestisci l'eccezione se l'utente inserisce 0 come secondo numero.
"""

numero_1 = input("Inserisci primo numero: ")
numero_2 = input("Inserisci secondo numero: ")

try:
    value_1 = int(numero_1)
    value_2 = int(numero_2)
except ValueError as err:
    print(err)
    raise("Valore/i non convertibile/i")

try:
    print(f"Divisone: {value_1/value_2}")
except ZeroDivisionError as err:
    print(err)
    raise("Impossibile dividere per zero")