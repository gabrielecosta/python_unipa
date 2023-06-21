class Persona():
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

    def id(self):
        return self.nome + " " + self.cognome + ". Matricola: " + self.matricola

class Studente(Persona):
    def __init__(self, nome, cognome, matricola, esami=None):
        super().__init__(nome,cognome,matricola)
        if esami is None:
            self.esami = []
        else:
            self.esami = esami

    def print_carrier(self):
        stringa = super().id()
        print(f"Studente {stringa}")
        if len(self.esami)==0:
            print("Non ha ancora sostenuto esami")
        else:
            for elem in self.esami:
                for (key, mark) in elem.items():
                    print(f"Materia: {key}, Voto: {mark}")
        import functions as fun
        marks = []
        for elem in self.esami:
            for (key, mark) in elem.items():
                marks.append(mark)
        media = fun.media(marks)
        print(f"Media: {media}")

    def add_exam(self, subject, mark):
        flag = True
        for elem in self.esami:
            if subject in elem:
                flag = False
        if flag:
            self.esami.append({subject:mark})

    def remove_exam(self, subject):
        flag = True
        for elem in self.esami:
            if subject in elem:
                value = elem[subject]
                self.esami.remove({subject:value})

            
    def save_file(self):
        marks = []
        for elem in self.esami:
            for (key, mark) in elem.items():
                marks.append(mark)
        import functions as fun
        media = fun.media(marks)
        import os
        filename = os.getcwd() + "\studenti" + "\libretto_" + self.nome + "_" + self.cognome + "_" + self.matricola + ".txt"
        with open(filename, 'w') as f:
            print(f"Nome: {self.nome}, Cognome: {self.cognome}, Matricola: {self.matricola}", file=f)
            if len(self.esami)==0:
                print("Non ha ancora sostenuto esami", file=f)
            else:
                for elem in self.esami:
                    for (key, mark) in elem.items():
                        print(f"Materia: {key}, Voto: {mark}", file=f)
            print(f"Media aritmetica: {media}", file=f)
            print("Università degli Studi di Palermo", file=f)

class Professore(Persona):
    def __init__(self, nome, cognome, matricola, materie=None):
        super().__init__(nome,cognome,matricola)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def print_carrier(self):
        stringa = super().id()
        print(f"Docente {stringa}")
        if len(self.materie)==0:
            print("Non insegna ancora")
        else:
            for elem in self.materie:
                for (key, code) in elem.items():
                    print(f"Materia: {key}, Codice: {code}")

    def add_subject(self, subject, code):
        flag = True
        for elem in self.materie:
            if subject in elem:
                flag = False
        if flag:
            self.materie.append({subject:code})

    def remove_subject(self, subject):
        flag = True
        for elem in self.materie:
            if subject in elem:
                value = elem[subject]
                self.materie.remove({subject:value})

    def save_file(self):
        import os
        filename = os.getcwd() + "\docenti" + "\libretto_" + self.nome + "_" + self.cognome + "_" + self.matricola + ".txt"
        with open(filename, 'w') as f:
            print(f"Nome: {self.nome}, Cognome: {self.cognome}, Matricola: {self.matricola}", file=f)
            if len(self.materie)==0:
                print("Non insegna ancora", file=f)
            else:
                for elem in self.materie:
                    for (key, code) in elem.items():
                        print(f"Materia: {key}, Codice: {code}", file=f)
            print("Università degli Studi di Palermo", file=f)



class Utenza():
    def __init__(self, utenza=None):
        if utenza is None:
            self.utenza = []
        else:
            self.utenza = utenza
    
    def cerca_studente(self, matricola):
        for elem in self.utenza:
            if type(elem) == Studente:
                if elem.matricola == matricola:
                    return elem
        return None
    

    def cerca_professore(self, matricola):
        for elem in self.utenza:
            if type(elem) == Professore:
                if elem.matricola == matricola:
                    return elem
        return None
    
    def aggiungi_studente(self, nome, cognome, matricola):
        stu = Studente(nome, cognome, matricola)
        self.utenza.append(stu)

    def aggiungi_professore(self, nome, cognome, matricola):
        pro = Professore(nome, cognome, matricola)
        self.utenza.append(pro)

    def aggiuni_materia_erogata(self, matricola, subject, codice):
        elem = self.cerca_professore(matricola)
        if  elem is not None:
            elem.add_subject(subject, codice)
        else:
            print("Utente non trovato")

    def aggiungi_esame_sostenuto(self, matricola, esame, voto):
        elem = self.cerca_studente(matricola)
        if elem is not None:
            elem.add_exam(esame, voto)
        else:
            print("Utente non trovato")

    def stampa_carriera_studente(self, matricola):
        elem = self.cerca_studente(matricola)
        if elem is not None:
            elem.print_carrier()
            elem.save_file()
        else:
            print("Utente non trovato")

    def stampa_carriera_professore(self, matricola):
        elem = self.cerca_professore(matricola)
        if elem is not None:
            elem.print_carrier()
            elem.save_file()
        else:
            print("Utente non trovato")

    def stampa_utenza(self):
        for elem in self.utenza:
            print(elem.id())