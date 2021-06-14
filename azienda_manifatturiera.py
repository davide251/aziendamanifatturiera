class modello():
    def __init__(self,nome,desrizione):
        self.nome
        self.descrizione

        def modifica_modello(self,modello):
            self.modello = modello
            print("modificato")


    class Catalogo():
        def __init__(self,nome):
            self.nome=nome
            self.modello=list()

        def aggiungi_modello(self,modello):
            self.modello.append(modello)
            print("modello aggiunto")

        def cancella_modello(self,modello):
            if modello in self.modello:
                self.modello.delete(modello)
                print("modello rimosso")

            else:
                 print("modello non presente")

        def cerca_modello(self,nome):
             for modello in self.modello:
              if modello.nome == nome:
                 print("modelli trovati:")
                 modello.stampa_info()

        def stampa_catalogo(self):
            for modello in self.modello:
                modello.stampa_info()
     
       
        prodotto=Catalogo()
        prodotto1.modello("xsd","tyyt","dipartimento1")
        prodotto2.modello("xpd","tyyt","dipartimento2")
        prodotto.aggiungi_modello(prodotto)
        prodotto.stampa_Catalogo()






    