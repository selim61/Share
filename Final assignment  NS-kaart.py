def inlezen_beginstation(stations):
    'Vraagt om het beginstation'

    while True:
        beginstation = input("Wat is uw beginstation?\n>> ")
        if beginstation in stations:
            print('Beginstation: {}'.format(beginstation))
            break
        else:
            print('Deze trein komt niet in {}'.format(beginstation))
    return beginstation

def inlezen_eindstation(stations, beginstation):
    'Vraagt om het eindstation'

    while True:
        eindstation = input("Wat is uw eindstation?\n>> ")
        if eindstation in stations:
            print('Eindstation: {}'.format(eindstation))
            break
        elif eindstation == beginstation:
            print('{} is al uw begin station'.format(eindstation))
            continue
        else:
            print('Deze trein komt niet in {}'.format(eindstation))
    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    'Print het stations nummer, prijs, beginstation, tussenstops, eindstation, etc.'
    beginindex = stations.index(beginstation)
    eindindex = stations.index(eindstation)
    print("",
          "Het beginstation {} is het {}e station in het traject.".format(beginstation, beginindex+1),
          "Het eindstation {} is het {}e station in het traject.".format(eindstation, eindindex+1),
          "De afstand bedraagt {} station(s).".format(abs(beginindex-eindindex)),
          "De prijs van het kaartje is {} euro.".format(abs(beginindex-eindindex)*5),
          sep="\n")
    tussenstops = []
    for i in range(beginindex+1, eindindex):
        tussenstops.append(stations[i])
    print("Jij stapt in de trein in: {}".format(beginstation))
    for stop in tussenstops:
        print(" - {}".format(stop))
    print("Jij stapt uit in: {}".format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
begin = inlezen_beginstation(stations)
eind = inlezen_eindstation(stations, begin)
omroepen_reis(stations, begin, eind)