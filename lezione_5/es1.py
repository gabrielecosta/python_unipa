"""
Scrivere le seguenti funzioni:
- all_the_same(x,y,z) che ritorna true se tutti gli argomenti sono uguali
- all_different(x,y,z) che ritorna True se tutti gli argomenti sono diversi
- all_sorted(x,y,z) che ritorna True se tutti gli argomenti sono in ordine crescente
"""
import sys

def all_the_same(x,y,z):
    """
    Funzione all_the_same(x,y,z)
    Ritorna true se tutti gli argomenti sono uguali
    """
    if (x == y and y == z):
        return True
    else:
        return False
    
def all_different(x,y,z):
    """
    Funzione all_different(x,y,z)
    Ritorna True se tutti gli argomenti sono diversi
    """
    if(x != y and x != z and y != z):
        return True
    else:
        return False
    
def all_sorted(x,y,z):
    """
    Funzione all_sorted(x,y,z)
    Ritorna True se tutti gli argomenti sono in ordine crescente
    """
    if (x<y and y<z):
        return True
    else:
        return False
    
def main():
    value = input("Inserisci valore:")
    if value.isdigit():
        x = int(value)
    else:
        sys.exit("Valore non valido")
    value = input("Inserisci valore:")
    if value.isdigit():
        y = int(value)
    else:
        sys.exit("Valore non valido")
    value = input("Inserisci valore:")
    if value.isdigit():
        z = int(value)
    else:
        sys.exit("Valore non valido")

    help(all_the_same)
    print(all_the_same(x,y,z))
    help(all_different)
    print(all_different(x,y,z))
    help(all_sorted)
    print(all_sorted(x,y,z))

if __name__ == "__main__":
    main()