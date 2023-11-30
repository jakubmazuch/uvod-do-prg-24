def spocitej_radky(cesta):
    pocet = 0
    with open(cesta, 'r', encoding='utf-8') as file:
        for row in file:
            pocet += 1
        return pocet
    file.close()


soubor = 'jmena.csv'
pocet_studentu = spocitej_radky(soubor)
print(pocet_studentu)
