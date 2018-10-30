total = []
while True:
    nummer = int(input("Geef een nummer: "))
    if nummer == 0:
        break
    total.append(nummer)
print("Er zijn {} getallen ingevoerd, de som is: {}".format(len(total), sum(total)))