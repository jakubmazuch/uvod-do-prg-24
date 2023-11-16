def vyber(m, hodnoty):
    pocty = []
    for i in hodnoty:
        pocet = m//i
        m = m - i*pocet
        pocty.append(pocet)
    return pocty


def vypis(hodnoty, pocty):
    for i, hodnota in enumerate(hodnoty):
        print(f"{hodnota}: {pocty[i]}")


# bankomat
B = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# uživatel si zadává kolik chce vybrat
m = int(input("Kolik korun chcete vybrat? "))

pocty = vyber(m, B)
vypis(B, pocty)
