import random

# Zadání mezí
a = int(input("Zadejte jednu mez: "))
b = int(input("Zadejte druhou mez: "))

w = 0 

if b < a:
    w = a
    a = b
    b = w

cislo = random.randint(a, b)
skore = 0
w = int(input("Hádej číslo! "))
while w != cislo:
    if w > cislo:
        print("Myslím si číslo, které je menší, než ", w)
    else:
        print("Myslím si číslo, které je větší, než ", w)
    
    w = int(input("Hádej číslo! "))
    skore += 1

print("Bingo! (skore: ", skore, ")")