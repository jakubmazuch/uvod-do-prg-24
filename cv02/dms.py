# deg, min, sec to dec
d = int(input("Zadej stupne: "))
m = int(input("Zadej minuty: "))
s = int(input("Zadej sekundy: "))
dec = d + m/60 + s/3600
print("Úhel: ", dec)

# dec to deg, min, sec
d2 = int(dec)
m2 = int((dec - d2) * 60)
s2 = ((dec - d2) * 60 - m2) * 60

print("Deg: ", d2)
print("Min: ", m2)
print("Sec: ", s2)
