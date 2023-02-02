#6.2
print()
print("tehtävä 2")
print()

# muokkaa edellinen funktio saamaan parametrinaan nopan tahkojen yhteismäärän
# pääohjelmassa nopan heittelyä jatketaan kunnes saadaan nopan maksimisilmäluku
# maksimisilmäluku kysytään käyttäjältä ohjelman suorituksen alussa


import random

tahkot = int(input("Annan arpakuution tahkojen määrä: "))
def heitto(tahkot):
    return random.randint(1,tahkot)

result = 0
while result != tahkot:
    result = heitto(tahkot)
    print(f"Arpakuution tulos: {result}")

print("Ohjelman suoritus loppui.")