import sys

def scambia_primo_ultimo(lista):
    """
    Questa funzione scambia primo e ultimo valore della lista
    """
    lista[0], lista[-1] = lista[-1], lista[0]

def shift_destra(lista):
    """
    Questa funzione shifta a destra tutti i valori della lista
    """
    turn = lista[0]
    for i in range(len(lista)):
        lista[(i+1)%len(lista)], turn = turn, lista[(i+1)%len(lista)]

def shift_sinistra(lista):
    """
    Questa funzione shifta a sinistra tutti i valori della lista
    """
    turn = lista[0]
    for i in range(len(lista)-1,-1,-1):
        lista[i], turn = turn, lista[i]

def sostituisci(lista, value=0):
    """
    Questa funzione sostituisce gli elementi pari della lista con value che di default è 0
    """
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            lista[i]=value

def second_max(lista):
    """
    Questa funzione ritorna il massimo e il secondo massimo
    """
    max_1 = max(lista)
    max_2 = lista[0]
    for elem in lista:
        if elem > max_2 and elem!=max_1:
            max_2 = elem
    return max_1, max_2


def somma_senza_minimo(lista):
    """
    Questa funzione ritorna la somma escluso l'elemento più piccolo
    """
    minval = min(lista)
    somma = sum(lista)
    return somma-minval

def is_crescente(lista):
    """
    Questa funzione ritorna True se la lista è ordinata in senso crescente
    """
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            return False
    return True

def ha_duplicati(lista):
    """
    Questa funzione ritorna True se contiene dei duplicati
    """
    for elem in lista:
        count = 0
        for i in range(len(lista)):
            if lista[i]==elem:
                count+=1
        if count>1:
            return True
    return False


def ha_duplicati_adiacenti(lista):
    """
    Questa funzione ritorna True se contiene elementi duplicati adiacenti
    """
    if ha_duplicati(lista):
        for i in range(len(lista)-1):
            if lista[i]==lista[i+1]:
                return True
        return False
    else:
        return False