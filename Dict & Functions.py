def namen():
    allenamen = {}
    while True:
        naam = input("Volgende naam: ")
        if naam == '':
            break
        else:
            if naam in allenamen:
                allenamen[naam] += 1
            else:
                allenamen[naam] = 1

    return allenamen.items()

for i in namen():
    if i[1] == 1:
        print("Er is {} student met de naam {}".format(i[1], i[0]))
    else:
        print("Er zijn {} studenten met de naam {}".format(i[1], i[0]))