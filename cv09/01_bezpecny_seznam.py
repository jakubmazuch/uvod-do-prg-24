def test_index(data, index):
    try:
        print(data[index])
    except IndexError:
        print("Chyba.")


seznam = [1, 2, 3, 4, 5, 6, 7, 8]
vstup = int(input("Vložte index, jehož hodnotu si žádáte zobrazit: "))
test_index(seznam, vstup)
