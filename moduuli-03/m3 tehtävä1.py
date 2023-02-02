#3.1
print("tehtävä 1")
print()

#kysy kuhan pituus → laske kuha veteen jos se on alle 37cm ja kerro paljonko puuttuu

lenght = int(input("Anna kuhan pituus: "))
print()

if lenght < 37:
    print("Kuha on " + str(37 - lenght) + " senttiä alimittainen")
    print("Laske kuha takaisin veteen.")

else:
    print("Voit nostaa kuhan!")