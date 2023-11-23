def bezpecny_vstup():
    while True:
        try:
            vstup = int(input("Zadejte cele číslo: "))
            return vstup
        except ValueError:
            print("To není číslo.")


cislo = bezpecny_vstup()
print("Požadavané číslo je: ", cislo+1)
