"""
chiedere all'utete di inserire un valore richiedendo esplicitamente
una virgola separatrice delle migliaia. Poi,
stampare il numero senza virgola
"""

value = input("Inerisci un valore con la virgola delle migliaia: ")

end = len(value)

centinaia = value[-3:end]

migliaia = value[0:-4]

print(f"Centinaia: {centinaia} \nMigliaia: {migliaia}")

number = int(migliaia)*1000 + int(centinaia)

print("Numero: ", number)
