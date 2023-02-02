#6.6
print()
print("tehtävä 6")
print()

# funktio saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä ja pizzan hinnan euroina
# funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri
# pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat
# ja ilmoittaa kummalla on alhaisempi yksikköhinta
# hyödynnä yksikköhintojen laskennassa funktio

import math


def priceperpizzasqm(d, price):
    d = d / 100
    A = math.pi * (d / 2)**2
    price_p_sm = price/A
    return price_p_sm


d = float(input("Anna pizzan halkaisija(cm): "))
price = float(input("Anna pizzan hinta(e): "))

result_one = priceperpizzasqm(d, price)

print()
d_two = float(input("Anna toisen pizzan halkaisija(cm): "))
price_two = float(input("Anna toisen pizzan hinta(e): "))

result_two = priceperpizzasqm(d_two, price_two)

print()

if result_one < result_two:
    print("Ensimmäisen ilmoittamasi pizzan yksikköhinta on pienempi.")
    print(f"Se maksaa {result_one:.2f} euroa/neliömetri.")

else:
    print("Jälkimmäisen ilmoittamasi pizzan yksikköhinta on pienempi.")
    print(f"Se maksaa {result_two:.2f} euroa/neliömetri.")

