def ticker(filename):
    infile = open(filename, 'r')
    lines = infile.readlines()
    tickerdict = {}
    for line in lines:
        values = line.split(":")
        tickerdict[values[0]] = values[1].rstrip()
    return tickerdict

def tickercompany(tickernaam):
    dict = ticker("ticker.txt")
    bedrijfnaam = ""
    for i in dict:
        if dict[i] == tickernaam:
            bedrijfnaam = i
            break
    return bedrijfnaam

def bedrijfticker(bedrijfnaam):
    dict = ticker("ticker.txt")
    tickernaam = ""
    for i in dict:
        if i == bedrijfnaam:
            tickernaam = dict[i]
            break
    return tickernaam

while True:
    print("1. Bedrijfsnaam naar Ticker\n2. Ticker naar Bedrijfsnaam")
    keuzen = int(input("Kies een optie: "))
    if keuzen == 1:
        cnaam = input("Voer bedrijfsnaam in: ")
        print("Ticker symbol: {}".format(bedrijfticker(cnaam)))
    elif keuzen == 2:
        tnaam = input("Voer Ticker symbol in: ")
        print("bedrijf naam: {}".format(tickercompany(tnaam)))
    else:
        break