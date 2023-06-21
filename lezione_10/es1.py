import es
import lezione_9.es2 as Imp

imp1 = Imp.Impiegato("Marco", "Rossi", 1400)
imp1.id()
Imp.Impiegato.numero_impiegati()

imp2 = Imp.Impiegato("Carlo", "Neri", 1800)
imp2.id()
Imp.Impiegato.numero_impiegati()

svl1 = es.Sviluppatore("Giuseppe", "Verdi", 100, "java")
svl1.id()
Imp.Impiegato.numero_impiegati()

manager = es.Manager("Gabriele", "Costa", 100, [imp1, imp2, svl1])
manager.id()
Imp.Impiegato.numero_impiegati()

svl1.print_job()

print(imp1)
print(svl1)
print(manager)

manager.stampa_supervisionati()

imp3 = es.Manager("gg", "gg", 5)
Imp.Impiegato.numero_impiegati()

manager.aggiungi_supervisionato(imp3)

print(imp3)

manager.stampa_supervisionati()

manager.rimuovi_supervisionato(imp3)

manager.stampa_supervisionati()

