#7.1
print()
print("tehtävä 1")
print()

# kysy kuukauden numero ja tulosta vastaava vuodenaika
# tallenna kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen
# määritellään kkukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi


# monikko eli tuple:
vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero: "))


if kuukausi == 1 or kuukausi == 2 or kuukausi == 12:
    vuodenaika = vuodenajat[3]
elif kuukausi >= 3 and kuukausi <= 5:
    vuodenaika = vuodenajat[0]
elif kuukausi >= 6 and kuukausi <= 8:
    vuodenaika = vuodenajat[1]
elif kuukausi >= 9 and kuukausi <= 11:
    vuodenaika = vuodenajat[2]
else:
    print("Virheellinen arvo.")

print(f"Antamasi kuukausi kuuluu vuodenaikaan {vuodenaika}.")