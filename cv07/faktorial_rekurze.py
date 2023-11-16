def faktorial_r(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial_r(n-1)


cislo = int(input("Zadejte číslo: "))
print(cislo, "!=", faktorial_r(cislo))
