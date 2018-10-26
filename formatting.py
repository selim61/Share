def convert(celsius):
    return celsius*1.8+32

def table():
    print("  F      C")
    graden = '{0:5.1f}   {1:5.1f}'
    for g in range(-30, 50, 10):
        print(graden.format(convert(g), g))

table()