"""
Scrivere un programma che legga un file contenente due colonne di numeri in virgola mobile e stampi
la media di ciascuna colonna (esempio file input 1)
"""
import os 
print(os.getcwd())
filename = os.getcwd() + '\input.txt'
print(f"Filename: {filename}")

col1 = []
col2 = []

with open(filename, 'r') as f:
    for row in f:
        values = row.split()
        col1.append(float(values[0]))
        col2.append(float(values[1]))

print(f"Prima colonna: {col1}")
print(f"Seconda colonna: {col2}")
n = len(col1)

print(f"Media prima colonna: {sum(col1)/n}")
print("Media seconda colonna: {:.2f}".format(sum(col2)/n))