def kwadraten_som(grontgetallen):
    for n in grontgetallen:
        return [n ** 2 for n in grontgetallen if n > 0]

a = kwadraten_som([4, 5, 3, -81])
grontgetallen = sum(a)
print (grontgetallen)