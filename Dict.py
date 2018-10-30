dict = {'Jan': 9, 'Klaas': 10, 'Osman': 10, 'Kees': 9, 'Ricardo': 10, 'Mustafa': 7, 'Akif': 3, 'Yunus': 7}

for i in dict:
    if dict[i] > 9:
        print("{} heeft een {}!".format(i, dict[i]))
    else:
        continue