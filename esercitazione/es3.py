"""
3. Liste:
Scrivi un programma che prenda in input una lista di numeri e restituisca una lista contenente solo i numeri pari 
presenti nella lista.
"""

def inserisci_numer():
    stringa = input("Inserisci una sequenza di numeri separati da virgola: ")
    words = stringa.split()
    numbers = []
    print(f"Sequenza: {words}")
    for elem in words:
        elem = elem.strip(',')
        try:
            elem = int(elem)
            numbers.append(int(elem))
        except ValueError as err:
            print(err)
            raise("Errore nella conversione!")
    print(f"Sequenza di numeri: {numbers}")
    return numbers

def main():
    numbers = inserisci_numer()
    odd = [x for x in numbers if x%2 == 0]
    print(f"Numeri pari nella sequenza: {odd}")

if __name__=="__main__":
    main()