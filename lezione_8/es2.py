"""
Scrivere un programma che mantenga un dizionario in cui le chiavi sono nomi di studenti,
e i valori le valutazioni ricevute per un esame. Il programma deve chiedere all'utente se desidera aggiungere
o rimuovere studenti, modificare valutazioni o stampare tutte le valutazioni.
"""
def stampa(dizionario):
    for (key,value) in dizionario.items():
        print(f"{key}: {value}")

def aggiungi(dizionario, key, value):
    if key not in dizionario:
        dizionario[key]=value
        print(f"({key}:{value}) aggiunta al dizionario")
    else:
        print("Chiave già esistente")

def rimuovi(dizionario, key):
    if key in dizionario:
        dizionario.pop(key)
        print(f"({key}) rimossa dal dizionario")
    else:
        print("Chiave non trovata")

def modifica(dizionario, key, new_value):
    if key in dizionario:
        dizionario[key]=new_value
        print(f"({key}:{new_value}) modificata nel dizionario")
    else:
        print("Chiave non trovata")

def main():
    dizionario = {}
    while True:
        print("1. aggiungi al dizionario")
        print("2. rimuovi dal dizionario")
        print("3. modifica dizionario")
        print("4. stampa dizionario")
        print("5. exit")
        try:
            risp = int(input('Risposta: '))
        except ValueError as err:
            print(err)
            print("Valore di default: stampa")
            risp = 4
        if risp==1:
            key = input("Inserisci nome (chiave): ")
            value = input("Inserisci valutazione (valore): ")
            aggiungi(dizionario, key, value)
        if risp==2:
            key = input("Inserisci nome (chiave) da eliminare: ")
            rimuovi(dizionario, key)
        if risp==3:
            key = input("Inserisci nome (chiave) da modificare: ")
            value = input("Inserisci nuova valutazione (valore): ")
            modifica(dizionario, key, value)
        if risp==4:
            stampa(dizionario)
        if risp==5:
            break

if __name__=="__main__":
    main()