"""
Scrivere un programma che chiede all'utente di inserire delle matricole di studenti.
Ogni studente ha un nome, un cognome, una matricola e un elenco di materie date secondo la coppia
Materia: Voto. 
Il programma deve permettere di inserire per ogni studente una materia da sostenere.
Il programma deve permettere inoltre di stampare l'elenco degli studenti e per ogni studente,
su richiesta, di stampare il libretto con un file, contenente anche la media aritmetica dei voti.
Si possono inserire anche i professori, ma l'elenco non sarà di materie sostenute, bensì di materie
insegnate con Materia: Corso
"""

import classes as cl

utenza = cl.Utenza()

while True:
    print("1. Inserisci studente")
    print("2. Inserisci professore")
    print("3. Inserisci materia da erogare")
    print("4. Inserisci esame sostenuto")
    print("5. Stampa carriera studente")
    print("6. Stampa carriera professore")
    print("7. Stampa utenza")
    print("8: esci")
    try:
        risp = int(input("Inserisci risposta: "))
    except ValueError:
        print("Errore di inserimento! Valore di default 7")
        risp = 7
    if risp==1:
        nome = input("Inserisci nome: ")
        cognome = input("Inserisci cognome: ")
        matricola = input("Inserisci matricola: ")
        utenza.aggiungi_studente(nome, cognome, matricola)
    elif risp == 2:
        nome = input("Inserisci nome: ")
        cognome = input("Inserisci cognome: ")
        matricola = input("Inserisci matricola: ")
        utenza.aggiungi_professore(nome, cognome, matricola)
    elif risp == 3:
        matricola = input("Inserisci matricola: ")
        materia = input("Inserisci materia: ")
        codice = input("Inserisci codice corso: ")
        utenza.aggiuni_materia_erogata(matricola, materia, codice)
    elif risp == 4:
        matricola = input("Inserisci matricola: ")
        esame = input("Inserisci esame: ")
        try:
            voto = int(input("Inserisci voto esame: "))
            utenza.aggiungi_esame_sostenuto(matricola, esame, voto)
        except ValueError as err:
            print(err)
            print("Esame non aggiunto")
    elif risp == 5:
        matricola = input("Inserisci matricola: ")
        utenza.stampa_carriera_studente(matricola)
    elif risp == 6:
        matricola = input("Inserisci matricola: ")
        utenza.stampa_carriera_professore(matricola)
    elif risp == 7:
        utenza.stampa_utenza()
    elif risp == 8:
        break
    else:
        print("Scelta non valida...")

"""
st1 = cl.Studente("Gabriele", "Rossi", "0712")

st1.print_carrier()

st1.add_exam("Analisi", 25)
st1.add_exam("Geometria", 21)
st1.add_exam("Geometria", 25)

st1.print_carrier()

st1.remove_exam("Geometria")

st1.print_carrier()

st1.add_exam("Tds", 30)

st1.print_carrier()

st1.save_file()


pr1 = cl.Professore("Giuseppe", "Verdi", "1025")

pr1.print_carrier()

pr1.add_subject("Analisi", "015")

pr1.print_carrier()

pr1.save_file()

"""