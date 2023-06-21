"""
Chiedere all'utente di inserire due numeri e di stamparne poi:
1. la somma e la differenza
2. il prodotto e la media
3. la distanza (valore assoluto)
4. il minimo e il massimo
"""

x = int(input("Inserisci primo valore: "))
y = int(input("Inserisci secondo valore: "))

print("Somma: ", x+y)
print("Differenza: ", x-y)
print("Distanza: ", abs(x-y))
print("Minimo: {0} \nMassimo: {1}".format(min(x,y), max(x,y)))
print("Prodotto: ", x*y)
print("Media: {:.2}".format((x+y)/2))
print("Divisione intera: ", x // y)
print("Resto: ", x % y)