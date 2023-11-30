import csv
from datetime import datetime


vstup = 'jmena.csv'
vystup = 'jmena_vek.csv'


def vypocet_veku(datum_nar):
    dnes = datetime.now()
    narozeni = datetime.strptime(datum_nar, '%d.%m.%Y')
    vek = dnes.year - narozeni.year
    return vek


# čtení vstupu a zpracování dat
vystupni_data = []
with open(vstup, mode='r', encoding='utf-8') as soubor:
    csv_ctecka = csv.reader(soubor, delimiter=';')
    for radek in csv_ctecka:
        jmeno, datum_narozeni = radek
        vek = vypocet_veku(datum_narozeni)
        vystupni_data.append([jmeno, vek])

# zápis výstupních dat do souboru
with open(vystup, mode='w', newline='', encoding='utf-8') as vsoubor:
    csv_zapis = csv.writer(vsoubor)
    for radek in vystupni_data:
        csv_zapis.writerow(radek)
