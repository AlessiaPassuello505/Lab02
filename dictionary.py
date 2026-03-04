import re
class Dictionary:
    def __init__(self,nomefile="dictionary.txt"):
        self.nome=nomefile
        self.dati={}
        try:
            with open(nomefile,"r", encoding="utf-8") as f:
                for riga in f:
                    campi=riga.strip().split()
                    if len(campi)==2:
                        self.dati[campi[0].lower()]=campi[1].lower()
        except FileNotFoundError:
            pass

    def addWord(self,tupla):
        aliena=tupla[0].lower()
        umane=tupla[1].lower()
        if aliena.isalpha() and umane.isalpha():
            if aliena.lower() not in self.dati:
                self.dati[aliena.lower()]=umane.lower()
                with open(self.nome, "a", encoding="utf-8") as f:
                    f.write(f"{aliena.lower()} {umane.lower()}\n ")
                return True
            else:
                return False
        return False


    def translate(self, aliena):
        return self.dati.get(aliena.lower(), "Parola non trovata")


    def translateWordWildCard(self,aliena):
        aliena=aliena.replace("?",".")
        pattern=re.compile(aliena)
        mylist=[]
        for chiave in self.dati.keys():
            if pattern.match(chiave):
                mylist.append(self.dati[chiave])
        return mylist











