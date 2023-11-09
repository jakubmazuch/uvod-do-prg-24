def vypocet_faktorialu(cislo):
    fakt = 1
    for i in range (1, cislo+1):
        fakt *= i
    return fakt

cislo = int(input("Zadejte cislo: "))
print(cislo, "! = ", vypocet_faktorialu(cislo))