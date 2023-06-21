"""
Implementare una classe Studente. Uno studente ha un nome, e un punteggio totale
conseguito nei quiz. Scrivere un costruttore appropriato e i metodi aggiungi_quiz(punteggio)
e punteggio_medio(). Per l'ultimo metodo occorrerà tenere traccia del numero di quiz che lo studente ha sostenuto
"""

import es1_ as util

nome = input("Inserisci nome: ")
cognome = input("Inserisci cognome: ")
matricola = input("Inserisci matricola: ")

st1 = util.Studente(nome, cognome, matricola)

print(st1.id())

st1.aggiungi_quiz(10)
st1.aggiungi_quiz(30)
st1.aggiungi_quiz(20)

print(st1.id())

print(f"Punteggio medio: {st1.punteggio_medio}")

st1.stampa_libretto()

st2 = util.Studente('Carlo', 'Conti', '0258')

print(st2.id())

st2.aggiungi_quiz(10)
st2.aggiungi_quiz(30)

print(st2.id())

print(f"Punteggio medio: {st2.punteggio_medio}")

st2.stampa_libretto()
