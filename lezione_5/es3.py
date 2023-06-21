"""
Scrivere la funzione repeat(string,n,delim) che ritorna la stringa
string ripetuta n volte, separate dalla stringa delim.
Per esempio: repeat('ho',3,',') deve ritornare la stringa 'ho, ho, ho'
"""

def repeat(string, n, delim):
    """
    Function: repeat(string, n, delim)
    Example: repeat('ho',3,',') deve ritornare la stringa 'ho, ho, ho'
    """
    ret = " "
    for i in range(n):
        ret += string
        if i != n-1:
            ret += delim
    return ret

def main():
    value = input("Inserisci stringa: ")
    n = int(input("Per quante volte ripetere: "))
    delim = input("Delimitatore: ")
    print(repeat(value,n,delim))

if __name__=="__main__":
    main()