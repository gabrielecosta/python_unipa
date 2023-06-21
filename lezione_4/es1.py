"""
Scrivere un programma che legga una sequenza di numeri interi e stampi:
- il valore più piccolo e quello più grande
- la quantità di numeri pari e dispari
- i totali cumulativi. Es: se gli input sono 1 7 2 9 il programma dovrà stampare 1 8 10 19
- tutti i duplicati adiacenti. Per esempio, se l'input è 1 3 3 4 5 5 6 6 6 2, il programma dovrà stampare 3 5 6
"""

value = input("Inserisci valore o digita exit per terminare: ")
risp = value if value!="exit" else "exit"
value = int(value) if value!="exit" else 0

smallest = value
largest = value
count = 0
odd = 0
even = 0

values = ""

while risp!="exit":
    values = values + str(value)
    count = count + value
    if value % 2 == 0:
        even+=1
    else:
        odd+=1
    print(count)
    value = input("Inserisci valore o digita exit per terminare: ")
    risp = value if value!="exit" else "exit"
    value = int(value) if value!="exit" else 0

print(f"Odd numbers: {odd} \nEven numbers: {even} \nCounter: {count}")
print("Valore duplicato: ")
for i in range(len(values)-1):
    if values[i]==values[i+1]:
        if i!=0:
            if values[i]!=values[i-1]:
                print(values[i], end=' ')
        if i==0:
            print(values[i], end=' ')