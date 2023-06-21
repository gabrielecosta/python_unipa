"""
Scrivere un programma che chieda all'utente di inserire un insieme
di numeri in virgola mobile. Quando l'utente inserisce un valore non numerico,
il programma da una seconda chance di inserire un valore corretto. Dopo due chances,
il programma smette di leggere l'input.
Il programma stampa in ogni caso, la somma di tutti i valori correttamente specificati.
Utilizzare la gestione delle eccezzioni per gestire input non corretti
"""

values = []

while True:
    try:
        value = float(input("Inserisci un valore in virgola mobile: "))
        values.append(value)
    except ValueError as err:
        print(err)
        try:
            value = float(input("Seconda chance: "))
            values.append(value)
        except ValueError as err:
            print(err)
            break

print(f"Valori inseriti: {values}")
print(f"Somma dei valori inseriti: {sum(values)}")