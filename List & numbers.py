invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst = invoer.split("-")
for i in range(len(lijst)):
    lijst[i] = int(lijst[i])
lijst.sort()
hoogstegetal = max(lijst)
laagstegetal = min(lijst)
hoeveelgetallen = len(lijst)
opgeteld = sum (lijst)
gemiddeld = sum(lijst)/len(lijst)

print("Gesorteerde list van ints: {}".format(lijst))
print("Grootste getal: {} en kleinste getal: {}".format(hoogstegetal, laagstegetal))
print("Aantal getallen: {} en Som van de getallen: {}".format(hoeveelgetallen, opgeteld))
print("Gemiddelde: {}".format(gemiddeld))