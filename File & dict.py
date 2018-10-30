def ticker(filename):
    infile = open(filename, 'r')
    lines = infile.readlines()
    tickerdict = {}
    for line in lines:
        values = line.split(":")
        tickerdict[values[0]] = values[1].rstrip()
    return tickerdict

def tickercompany(tickername):
    dict = ticker("ticker.txt")
    companyname = ""
    for i in dict:
        if dict[i] == tickername:
            companyname = i
            break
    return companyname

def companyticker(companynaam):
    dict = ticker("ticker.txt")
    tickernaam = ""
    for i in dict:
        if i == companynaam:
            tickernaam = dict[i]
            break
    return tickernaam

while True:
    print("1. Company to Ticker\n2. Ticker to Company")
    keuzen = int(input("Choose an option: "))
    if keuzen == 1:
        cnaam = input("Enter Company name: ")
        print("Ticker symbol: {}".format(companyticker(cnaam)))
    elif keuzen == 2:
        tnaam = input("Enter Ticker symbol: ")
        print("Company name: {}".format(tickercompany(tnaam)))
    else:
        break