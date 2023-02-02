#4.4
print()
print("tehtävä 4")
print()

#kirjoita peli, joka arpoo kokonaisluvun väliltä 1-10
#kysy lukua pelaajalta, kunnes se on oikein

import random
luku = int(random.randint(1,10))
arvaus = int(input("Arvaa lukua 1-10: "))

while arvaus != luku:
    if arvaus > luku:
        print("Luku on pienempi.")
        print()
    elif arvaus < luku:
        print("Luku on suurempi.")
        print()
    arvaus = int(input("Arvaa uudestaan: "))

print()
print("Oikein!")
