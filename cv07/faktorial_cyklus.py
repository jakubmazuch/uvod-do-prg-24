def faktorial(cislo):
    faktorial = 1
    for i in range(1, cislo+1):
        faktorial *= i
    return faktorial


cislo = int(input("Zadejte číslo: "))
print(cislo, "!=", faktorial(cislo))
