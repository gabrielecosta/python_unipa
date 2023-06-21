"""
Scrivere una funzione count_vowels(string) ch ritorna il numero
di vocali contenute nella stringa string
"""

def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"
    for letter in string:
        if letter in vowels:
            count += 1
    return count

def main():
    stringa = input("Inserisci una frase: ")
    print(f"Numero di vocali inserite: {count_vowels(stringa)}")

if __name__=="__main__":
    main()