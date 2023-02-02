#5.2
import math

print()
print("tehtävä 2")
print()

# kysy käyttäjältä lukuja, lopeta tyhjään
# tulosta viisi suurinta suuruusjärjestyksessä suurimmasta alkaen

luvut = []

luku = input("Anna luku: ")
if luku != "":
    luku = int(luku)

while luku != "":
    luvut.append(luku)
    luku = input("Anna uusi luku, lopeta painamalla Enter: ")
    if luku != "":
        luku = int(luku)

print()
print("Antamasi numerot:")
print(luvut)
print()
for n in luvut:
    luvut.sort(reverse=True)

print(f"Viisi suurinta luvut: {luvut[0:5]}")