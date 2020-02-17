import re
password = input("Wat is uw wachtwoord?: ")
x = True
punten = 0

while x:
    #checkt ofdat bepaalde tekens aanwezig zijn
    kleineletters = len(re.findall("[a-z]", password))*0.5
    groteletter = len(re.findall("[A-Z]", password))*1.5
    cijfers = len(re.findall("[0-9]", password))*2
    symbolen = len(re.findall("[$#@!?%]", password))*2.5

    #totale rekensom
    punten = kleineletters + groteletter + cijfers + symbolen

    #Einde While loop
    x = False

    # Deze regel geeft min punten als bepaalde dingen niet aanwezig zijn
    if (cijfers == 0 or symbolen == 0):
        punten = punten - 2
    if (groteletter == 0):
        punten = punten - 2

    # Deze regels geven het aantal punten aan. Daarnaast geeft het ook aan ofdat het wachtwoord zwak,gemiddeld of sterk is
    if (punten < 10):
        print("Je hebt "+ str(punten) + " punten behaald, dat betekend dat dit een zwak wachtwoord is")
    elif (punten >10 and punten <20):
        print("Je hebt "+ str(punten) + " punten behaald, dat betekend dat dit een gemiddeld sterk wachtwoord is")
    elif (punten > 20):
        print("Je hebt "+ str(punten) + " punten behaald, dat betekend dat dit een sterk wachtwoord is")





