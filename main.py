import translator as tr

t = tr.Translator()
t.loadDictionary("filename.txt")

while(True):

    t.printMenu()
    #input("Inserisci un numero:")
    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok quale parola devo aggiungere?")
        parola=input("Inserisci parola aliena e la sua traduzione")
        t.handleAdd(parola)

    if int(txtIn) == 2:
        print("Quale parola vuoi cercare?")
        parola= input("Inserisci parola: ")
        t.handleTranslate(parola)
        print(t.handleTranslate(parola))

    if int(txtIn) == 3:
        print("Quale parola vuoi cercare con wildcard?")
        parola = input("Inserisci parola: ")
        print(t.handleWildCard(parola))

    if int(txtIn) == 4:
        print("Esci")
        break
