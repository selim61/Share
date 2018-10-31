def even(l):
    evennummer = []
    for n in l:
        if n % 2 == 0:
            evennummer.append(n)
    return evennummer
print(even([1,2,3,4,5,6,7,8,9]))
