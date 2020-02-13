import re
password = input("Wat is uw wachtwoord?: ")
x = True
punten = 0
final = "test"

while x:
    if (len(password)<6):
        punten = punten - 10
    elif (len(password)>=6 and len(password)<=8):
        punten = punten + 10
    elif (len(password)>8):
        punten = punten + 15

    kleineletters = len(re.findall("[a-z]", password))
    groteletter = len(re.findall("[A-Z]", password))
    cijfers = len(re.findall("[0-9]", password))
    symbolen = len(re.findall("[$#@!?]", password))

    final = str(punten)
    x = False


    print("je hebt "+ final +" van de 35 punten " + str(counter))




