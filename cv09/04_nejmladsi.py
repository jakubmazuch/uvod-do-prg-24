def najit_nejmladsi_osobu(vstup):
    nejmladsi = None
    min_vek = float('inf')

    with open(vstup, 'r', encoding='utf-8') as soubor:
        for radek in soubor:
            jmeno, vek = radek.strip().split(',')
            vek = int(vek)

            if vek < min_vek:
                min_vek = vek
                nejmladsi = jmeno

    return nejmladsi, min_vek


soubor = 'jmena_vek.csv'
print(najit_nejmladsi_osobu(soubor))
