file = open('kaartnummers.txt', 'r')
namen = file.readlines()
for i in namen:
    split = i.split(", ")
    print("{} heeft kaartnummer: {}".format(split[1].replace('\n', ''), split[0]))