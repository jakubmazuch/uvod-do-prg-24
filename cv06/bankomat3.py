# bankomat
B = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# uživatel si zadává kolik chce vybrat
m = int(input("Kolik korun chcete vybrat?"))

pocty = []

for i in B:
    pocet = m//i
    m = m - i*pocet
    pocty.append(pocet)

for j, i in enumerate(B):
    print(f"{i}: {pocty[j]}")
