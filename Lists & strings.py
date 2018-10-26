lijst = eval(input("Geef lijst met minimaal 10 strings: "))
if len(lijst) <10:
    print("je hebt minder dan 10 strings")
else:
    lijst2 = []
    for woord in lijst:
        if len(woord) == 4:
            lijst2.append(woord)
    print(lijst2)