#4.2
print()
print("tehtävä2")
print()

#kysy tuumat, anna senttimetrit kunnes käyttäjä antaa negatiivisen luvun
# 1 tuuma = 2,54cm

tuuma = int(input("Anna luku tuumina: "))

while tuuma >= 0:
    cm = float(tuuma * 2.54)
    print(tuuma, "tuumaa on" , cm, " senttimetriä.")
    print()
    tuuma = int(input("Anna uusi luku tuumina: "))

print()
print("Toiminnot lopetettu.")
