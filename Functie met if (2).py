#Schrijf (en test) een functie new_password()
#die 2 parameters heeft:
# oldpassword en newpassword.
#De return-waarde is True als het nieuwe
# password voldoet aan de eisen.
# Het nieuwe password wordt alleen geaccepteerd
# als het verschilt van het oude password
# èn als het minimaal 6 tekens lang is.
# Als dat niet zo is,
# is de return-waarde False.

def new_password():
    oldpassword = input("vul je oude wachtwoord in: ")
    newpassword = input("vul je nieuwe wachtwoord in: ")
    if oldpassword == newpassword:
        print(False)
    if len(newpassword) < 6:
        print(False)
    else:
        print(True)

new_password()
