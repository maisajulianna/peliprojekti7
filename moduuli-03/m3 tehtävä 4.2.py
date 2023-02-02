#3.4
print()
print("tehtävä 4")
print()

#kysy vuosiluku, kerro onko se karkausvuosi

year = int(input("Anna vuosiluku: "))
print()

if year % 400 == 0:
    print("Vuosi on karkausvuosi.")
elif year % 100 == 0:
    print("Vuosi ei ole karkausvuosi.")
elif year % 4 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")