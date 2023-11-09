import math
def eratosthenovo_sito(n):
    n += 1
    sito = [True] * n    
    for i in range(2, int(math.sqrt(n))):
        if sito[i]:
            for j in range(i**2, n, i):
                sito[j] = False
    prvocisla = []
    for i in range(2,n):
        if sito[i]:
            prvocisla.append(i)
    return prvocisla

vstup = int(input("Zadejte mez: "))
print(eratosthenovo_sito(vstup))