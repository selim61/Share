def stemmen():
    leeftijd = input("Geef je leeftijd: ")
    paspoort = input("Nederlands paspoort: ")
    if int(leeftijd) >=18 and paspoort == "ja" or "Ja":
        print("Gefeliciteerd, je mag stemmen!")
    else:
        print ("Jammer je mag niet stemmen")

stemmen()