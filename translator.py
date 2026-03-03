import dictionary as diz

class Translator:

    def __init__(self):
        self.dati=diz.Dictionary()  #creo istanza

    def printMenu(self):
        print("STAMPA MENU:")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        diz.Dictionary(dict)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.dati.addWord(entry)


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        risposta= self.dati.translate(query)
        return risposta


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>

        pass