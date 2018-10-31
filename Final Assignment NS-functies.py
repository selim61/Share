def standaardprijs(afstandKM):
    if afstandKM <= 0:
        return 0
    elif afstandKM < 50:
        return afstandKM * 0.80
    elif afstandKM >= 50:
        return afstandKM * 0.60 + 15

def ritprijs(leeftijd, weekendrit, afstandKM):
    result = standaardprijs(afstandKM)
    leeftijdkorting = leeftijd <12 or leeftijd >=65

    if weekendrit and leeftijdkorting:
        return result * 0.65
    elif weekendrit and not leeftijdkorting:
        return result * 0.60
    elif not weekendrit and not leeftijdkorting:
        return result
    elif not weekendrit and leeftijdkorting:
        return result * 0.70


prijs = ritprijs(11, True, 80)
prijs1 = ritprijs(12, True, 80)
prijs2 = ritprijs(18, False, 80)
prijs3 = round(ritprijs(65, False, 80),2)
print (prijs3)