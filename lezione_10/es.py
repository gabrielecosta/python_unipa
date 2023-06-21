"""
Estendere la classe Impiegato dell'esercizio 2 della lezione 9. 
Derivare due sottoclassi: la classe Sviluppatore con un attributo per tenere traccia del linguaggio
di prgrammazione preferito. La classe Manager con un attributo per tenere traccia degli impiegati
che un certo Manager supervisiona.
"""
import lezione_9.es2 as lecture

class Sviluppatore(lecture.Impiegato):
    def __init__(self, nome, cognome, stipendio, linguaggio):
        super().__init__(nome, cognome, stipendio)
        self.linguaggio = linguaggio

    @property
    def email(self):
        stringa = super().email
        return stringa[0:-12] + self.linguaggio + ".azienda.com"
    
    def print_job(self):
        print(f"{self.nome} {self.cognome} è uno sviluppatore specializzato in {self.linguaggio}")
    
    def __repr__(self):
        return super().__repr__() + ", " + self.linguaggio


class Manager(lecture.Impiegato):
    def __init__(self, nome, cognome, stipendio, supervisionati=None):
        super().__init__(nome, cognome, stipendio)
        if supervisionati is None:
            self.supervisionati = []
        else:
            self.supervisionati = supervisionati

    @property
    def email(self):
        stringa = super().email[0:-11]
        return stringa + "manager" + ".azienda.com"

    def __repr__(self):
        return super().__repr__() + ", manager"
    
    def aggiungi_supervisionato(self, imp):
        self.supervisionati.append(imp)
    
    def rimuovi_supervisionato(self, imp):
        self.supervisionati.remove(imp)

    def stampa_supervisionati(self):
        print("Elenco supervisionati: ")
        for elem in self.supervisionati:
            print(elem)