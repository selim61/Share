bruin = {"Boxtel", "Best", "Beukenlaan", "Eindhoven", "Helmond 't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"}
groen = {"Boxtel", "Best", "Beukenlaan", "Eindhoven", "Geldrop", "Heeze", "Weert"}

zelfdehaltes = bruin.intersection(groen)
print(zelfdehaltes)

verschillendehalts = bruin.difference(groen)
print(verschillendehalts)

allehaltes = bruin.union(groen)
print(allehaltes)