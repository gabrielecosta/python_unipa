"""
Scrivere un programma che legga una stringa e stampi:
- solo le lettere maiuscole contenute nella stringa
- la stringa con tutte le vocali rimpiazzate da un underscore
- il numero di cifre nella stringa
"""

stringa = input("Inserisci stringa: \n")
vocals = "aeiou"

cipher = 0
stringa_ = ""

for i in range(len(stringa)):
    if stringa[i].isupper():
        print(stringa[i], end=' ')
    if stringa[i].isnumeric():
        cipher+=1
    if stringa[i].lower() in vocals:
        stringa_ += "_"
    else:
        stringa_ += stringa[i]
print()

print("Numero di cifre: ", cipher)
print(f"Stringa con gli underscore: {stringa_}")
