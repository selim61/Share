def gemiddelde(zin):
    woorden = zin.split(" ")
    tekst = len(woorden)
    letters = 0
    for woord in woorden:
        letters += len(woord)

    gemiddelde = letters/tekst
    print('de zin heeft {} woorden en elk woord heeft gemiddeld {:.2f} letters'.format(tekst, gemiddelde))


gemiddelde(input("vul een zin in: "))