def minmax(a):
    if not a:   # Ověřuje, že list není prázdný
        return None, None
    min = max = a[0]
    for cislo in a:
        if cislo > max:
            max = cislo
        if cislo < min:
            min = cislo 
    return min, max

#Testování
muj_seznam = []
minimum, maximum = minmax(muj_seznam)

print(f"Maximum: {maximum}, Minimum: {minimum}")