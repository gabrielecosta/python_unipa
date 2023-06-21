

class Studente:

    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.esami_sostenuti=0
        self.esami=set()

    def id(self):
        print(f"{self.nome} {self.cognome}, matricola: {self.matricola}")
        print("Esami sostenuti:")
        for elem in self.esami:
            print(f"{elem.punteggio}, {elem.matricola}")

    def aggiungi_quiz(self, punteggio):
        esame = Esame(punteggio, self.matricola)
        self.esami.add(esame)
        self.esami_sostenuti += 1
    
    @property
    def punteggio_medio(self):
        print(f"Esami convalidati: {self.esami_sostenuti}")
        val_tot = 0
        for esame in self.esami:
            val_tot += int(esame.punteggio)
        return (val_tot//self.esami_sostenuti)
    
    def stampa_libretto(self):
        with open(f'libretto{self.matricola}.txt', 'w') as f:
            print(f"Nome: {self.nome},\nCognome: {self.cognome},\nMatricola: {self.matricola}", file=f)
            for elem in self.esami:
                print(f"Esame sostenuto con valutazione: {elem.punteggio}", file=f)


class Esame:  
    def __init__(self, punteggio, matricola):
        self.punteggio = punteggio
        self.matricola = matricola