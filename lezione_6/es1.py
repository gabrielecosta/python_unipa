import operazioni as op
import sys

def main():
    lista = []
    while True:
        value = input("Inserisci un valore intero (exit per terminare): ")
        if value != "exit":
            if int(value):
                lista.append(int(value))
            else:
                sys.exit("valore non consentito")
        else:
            break
    print(lista)
    #scambia primo per ultimo
    op.scambia_primo_ultimo(lista)
    print(f"Scambia primo per ultimo. Output: {lista}")
    #shift a destra
    op.shift_destra(lista)
    print(f"Shifta a destra: {lista}")
    #shit a sinistra
    op.shift_sinistra(lista)
    print(f"Shift a sinistra: {lista}")
    #sostituisci con valore 2
    op.sostituisci(lista, 2)
    print(f"Sostituisci con valore 2: {lista}")
    #sostituisci con default
    op.sostituisci(lista)
    print(f"Sostituisci con default: {lista}")
    #stampa massimo e secondo massimo
    print(f"Massimo e secondo massimo: {op.second_max(lista)}")
    #somma senza minimo
    print(f"Somma senza il minimo: {op.somma_senza_minimo(lista)}")
    #is crescente
    print(f"Lista ordinata in senso crescente? {op.is_crescente(lista)}")
    #ha duplicati
    print(f"La lista ha duplicati? {op.ha_duplicati(lista)}")
    #ha duplicati adiacenti
    print(f"La lista ha duplicati adiacenti? {op.ha_duplicati_adiacenti(lista)}")

if __name__=="__main__":
    main()