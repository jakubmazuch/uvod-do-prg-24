a = int(input("Zadejte cislo:"))

if a < 10:
    print("Jednociferné")
elif a < 100:
    print("Dvojciferné")
elif a < 1000:
    print("Tříciferné")
elif a < 10000:
    print("Čtyřciferné")
else:
    print("Víceciferné")
