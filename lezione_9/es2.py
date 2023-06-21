"""
Implementare una classe Impiegato. Un impiegato ha un nome,un cognome,
un indirizzo email e uno stipendoi. Tutti gli oggetti della classe impiegato
condividono una certa quota percentuale di incremento stipendio annuale, che viene fissata dall'azienda.
Implementare il metodo aumento per applicare l'aumento annuale di stipendio.
Tenere traccia del numero di impiegati dell'azienda
"""

class Impiegato:

    quota_percentuale = 10.5

    impiegati = 0

    def __init__(self, nome, cognome, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio
        Impiegato.impiegati += 1
    
    
    @property
    def email(self):
        return self.nome + "." + self.cognome + "@azienda.com"

    def incremento_annuale(self):
        self.stipendio = self.stipendio + (self.stipendio*Impiegato.quota_percentuale)/100

    def id(self):
        return (f"Nome: {self.nome}, Cognome: {self.cognome}, Stipendio: {self.stipendio}, Email: {self.email}")

    @staticmethod
    def numero_impiegati():
        print(f"Attualmente in azienda sono assunti {Impiegato.impiegati} impiegati")

    def __repr__(self):
        return self.nome + " " + self.cognome + ", " + self.email
    
    @set
    def set_stipendio(self, value):
        self.stipendio = value
    

def main():
    imp1 = Impiegato("Mario", "Rossi", 100)
    imp2 = Impiegato("Carlo", "Verdi", 50)

    imp1.id()
    Impiegato.numero_impiegati()
    imp2.id()
    Impiegato.numero_impiegati()

    impiegati =  set()
    impiegati.add(imp1)
    impiegati.add(imp2)

    for imp in impiegati:
        imp.incremento_annuale()
        imp.id()
        
if __name__=="__main__":
    main()