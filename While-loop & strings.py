while True:
    string= (input("Geef een string met vier letters: "))
    if len(string) == 4:
        print("inlezen van correcte sting: {} is geslaagd".format(string))
        break
    print("{} heeft {} letters".format(string, len(string)))