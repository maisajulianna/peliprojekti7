#7.3
print()
print("Tehtävä 3")
print()

# kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi
# kysy käyttäjältä, haluaako tämä:
# 1 syöttää uuden lentoaseman, 2 hakea jo syötetyn lentoaseman tiedot vai 3 lopettaa



def lisaa():
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anna lentoaseman nimi: ")
    print()
    lentoasemat[tunnus] = nimi
    return


def hae():
    tunnus = input("Anna lentoaseman tunnus: ")
    if tunnus in lentoasemat:
        print(f"Lentoasema {tunnus} on {lentoasemat[nimi]}.")
    return




# pääohjelma:
# luodaan sanakirja, jolle annetaan yhden alkion


lentoasemat = {"Helsinki-Vantaan lentoasema" : "EFHK"}

toiminto = -1

while toiminto !=3:
    print("0 = lentoaseman tiedot")
    print("1 = lisää uusi lentoasema")
    print("2 = hae lentoasema")
    print("3 = lopeta")
    print()

    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 1:
        lisaa()
    elif toiminto == 2:
        hae()

print("Toiminnot lopetettu.")