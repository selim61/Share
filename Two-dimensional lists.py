studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    gemiddeldps= []
    for s in studentencijfers:
        gemiddeldps.append(sum(s)/len(s))
    return gemiddeldps

def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddeld = 0
    for s in studentencijfers:
        gemiddeld += (sum(s))/(len(s))
    return  gemiddeld/len(studentencijfers)

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))