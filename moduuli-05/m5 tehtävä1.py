#5.1
print()
print("tehtävä 1")
print()

import random

#kysy arpakuutioiden lukumäärä
#heitä kaikkia noppia kerran
#tulosta silmälukujen summa

arpakuutiot = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for i in range(arpakuutiot):
    heitto = random.randint(1, 6)
    print(f"Silmäluku: {heitto}")
    summa += heitto

print()
print("Silmälukujen summa on", summa)
