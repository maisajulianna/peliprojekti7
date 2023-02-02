#5.4
print()
print("tehtävä 4")
print()

# kysy viiden kaupungin nimet yksi kerrallaan
# tulosta kaupunkien nimet syöttöjärjestyksessä

kaupungit = []
toisto = 5

kaupunki = input("Anna kaupungin nimi: ")
kaupungit.append(kaupunki)

for i in kaupungit:
    kaupunki = input("Anna uuden kaupungin nimi: ")
    kaupungit.append(kaupunki)
    toisto -= 1
    if toisto == 1:
        break

print()
print("Nimeämäsi kaupungit:")

for kaupunki in kaupungit:
    print(kaupunki)