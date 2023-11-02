text = input("Zadejte text: ")
seznam = list(text)
opacne = []

# Projde seznam znaků od konce k začátku a přidá je do nového seznamu
for i in range(len(seznam) - 1, -1, -1):
    opacne.append(seznam[i])

vysl = ''.join(opacne)
print("Opačný text:", vysl)
