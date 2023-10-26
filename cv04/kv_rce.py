# DÚ: Upravte program dle zadaných gradací.

a = float(input("Zadejte hodnotu koeficientu u kvadratického členu: "))
b = float(input("Zadejte hodnotu koeficientu u lineárního členu: "))
c = float(input("Zadejte hodnotu koeficientu u absolutního členu: "))

D = b**2 - 4*a*c

if a != 0 and b != 0 and c != 0:
    if D > 0:
        x1 = (-b + D**(1/2)) / (2*a)
        x2 = (-b - D**(1/2)) / (2*a)             
        print(x1, x2)
    elif D == 0:
        x = (-b / (2*a))
        print(x)
    else:
        print("D je zaporné, není řešení na R")
else:
    print("Chyba.")
