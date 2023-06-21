"""
6. Set:
Scrivi un programma che prenda in input una lista di numeri e restituisca un set contenente solo i numeri unici 
presenti nella lista.
"""
import es3 as es

numbers = es.inserisci_numer()
new_set = set()
for elem in numbers:
    new_set.add(elem)
print(f"Numeri unici: {new_set}")
