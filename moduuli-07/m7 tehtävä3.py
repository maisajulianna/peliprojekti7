#7.3
print()
print("tehtävä 3")
print()

# kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi
# kysy käyttäjältä, haluaako tämä:
# 1 syöttää uuden lentoaseman, 2 hakea jo syötetyn lentoaseman tiedot vai 3 lopettaa



def lisaa():
    print()
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anna lentoaseman nimi: ")
    print()
    lentoasemat[tunnus] = nimi
    return


def hae_nimi():
    tunnus = input("Anna lentoaseman tunnus: ")
    if tunnus in lentoasemat:
        print(f"Lentoasema {tunnus} on {lentoasemat[tunnus]}.")
        print()
    return


def hae_tunnus():
    nimi = input("Anna lentoaseman nimi: ")
    if nimi in lentoasemat:
        print(f"Lentoaseman {nimi} tunnus on {lentoasemat[nimi]}.")
        print()
    return

# pääohjelma:

# luodaan sanakirja, jolle annetaan yksi alkio
lentoasemat = {"EFHK":"Helsinki-Vantaan lentoasema"}

toiminto = -1

while toiminto !=4:
    print("Valittavat toiminnot: ")
    print("1 = lisää uusi lentoasema")
    print("2 = hae lentoaseman nimi")
    print("3 = hae lentoaseman tunnus")
    print("4 = lopeta")
    print()

    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 1:
        lisaa()
    elif toiminto == 2:
        hae_nimi()
    elif toiminto == 3:
        hae_tunnus()

print("Toiminnot lopetettu.")