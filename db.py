import sqlite3
conn = sqlite3.connect('modelli.db')
curs = conn.cursor()

try:

    curs.execute("DROP table modello")
    curs.execute("DROP table catalogo")
except:
       pass
curs.execute("CREATE table modello (nome char(30), descizione char(30)")

class Catalogo():
    def __init__(self,nome,cursore):
        self.nome=nome
        self.modello=list()
        self.cursore =cursore

    def aggiungi_modello(self,modello):
        self.modello.append(modello)
        row = (modello.nome,modello.descrizione,self.nome)
        self.cursore.execute("insert into modello values()",row)
        print("modello aggiunto")

    def cancella_modello(self,modello):
            if modello in self.modello:
                self.modello.delete(modello)
                self.cursore.execute("delete from modello where nome = ?",(modello.nome))
                print("modello rimosso")
    
    def cerca_modello(self,nome):
             for modello in self.modello:
              if modello.nome == nome:
                 print("modelli trovati:")
                 modello.stampa_info()
                 self.cursore.execute("SELECT * FROM modello WHERE indirizzo = ?,"(modello.nome))
                 for row in self.cursore.fetchall():
                  print(row)

    def stampa_catalogo(self):
            for modello in self.modello:
                modello.stampa_info()
                self.cursore.execute("SELECT * FROM modello")
                for row in self.cursore.fetchall():
                  print(row)
    

    
