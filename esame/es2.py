class Studente:
    def __init__(self, nome, cognome, matricola):
        self.data = {
            'nome': nome,
            'cognome': cognome,
            'matricola': matricola
        }

    def fun9(self):
        n = int(self.data['matricola'][-2])
        x = 3
        if '2' in self.data['matricola']:
            x += 2
        if '8' in self.data['matricola']:
            x+=5
        return (x+n)%4
    
class StudenteTriennale(Studente):
    def __init__(self, nome, cognome, matricola):
        super().__init__(nome, cognome, matricola)
        self.flag = False

        if '1' in self.data['matricola']:
            self.flag = not self.flag
        if '9' in self.data['matricola']:
            self.flag = not self.flag

    def fun10(self):
        x = int(self.data['matricola'][-1])
        if self.flag:
            return (x*2)%4
        else:
            return (x+5)%4
        
st1 = StudenteTriennale('Gabriele', 'Costa', '0711990')
print(st1.fun10())