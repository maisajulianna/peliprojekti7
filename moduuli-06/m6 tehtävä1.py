#6.1
print()
print("tehtävä 1" )
print()

# funktio palauttaa satunnaisen nopan silmäluvun
# pääohjelma heittää noppaa kunnes tulee kutonen
# pääohjelma tulostaa kunkin heiton silmäluvun

import random

def heitto():
    return random.randint(1,6)

result = 0
while result != 6:
    result = heitto()
    print(f"Arpakuution tulos: {result}")

print("Ohjelman suoritus loppui.")
