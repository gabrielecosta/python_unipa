"""
Scrivere un programma che visualizzi sullo shcermo il proprio
nome all'interno di un reattangolo
"""
nome = input("Inserisci il tuo nome: ")
print("+---------------+")
print("|{:^15}|".format(nome))
print("+---------------+")