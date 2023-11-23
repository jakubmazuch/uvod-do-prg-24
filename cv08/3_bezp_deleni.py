def deleni(a, b):
    try:
        vysledek = a / b
        return vysledek
    except ZeroDivisionError:
        print("Nulou nelze dělit.")


delenec = int(input("Zadejte dělenec: "))
delitel = int(input("Zadejte dělitel: "))

print(deleni(delenec, delitel))
