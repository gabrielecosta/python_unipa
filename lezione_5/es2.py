"""
Scrivere la funzione middle(string) che ritorna una stringa contenente il carattere centrale
in string se la dimensione della stringa è dispari, altrimenti ritorna i due caratteri centrali
se la dimensione della stringa è pari.
Ad esempio: middle("middle") deve ritornare la stringa 'dd'
"""

def middle(string):
    size = len(string)
    if size % 2 == 0:
        #pari
        return string[(size//2-1):(size//2+1)]
    else:
        #dispari
        return string[size//2]

def main():
    string = input("Inserisci stringa: ")
    ret = middle(string)
    print(f"Valore di ritorno: {ret}")

if __name__ == "__main__":
    main()