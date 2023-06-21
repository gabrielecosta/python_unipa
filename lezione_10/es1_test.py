import unittest
import lezione_9.es2 as Imp

class ImpiegatoTest(unittest.TestCase):
    def setUp(self):
        print("Inizio test della classe impiegato sui metodi ID() e aumenta()")
        self.imp = Imp.Impiegato("Mario", "Rossi", 100)

    def test_id(self):
        expected = "Nome: {self.nome}, Cognome: {self.cognome}, Stipendio: {self.stipendio}, Email: {self.email}"
        self.assertEqual(self.id(), expected)

    def tearDown(self):
        return super().tearDown()