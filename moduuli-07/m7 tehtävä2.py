#7.2
print()
print("tehtävä 2")
print()

# kysy käyttäjältä nimiä tyhjään merkkijonoon asti
# nimen syöttämisen jälkeen ohjelma tulostaa tekstin 'uusi nimi' tai 'aiemmin syötetty nimi'
# lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä
# käytä joukkotietorakennetta

# set = joukko:
nimet = set()

nimi = input("Anna nimi, tyhjä lopettaa: ")

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(nimi)
    print()
    nimi = input("Anna nimi, tyhjä lopettaa: ")

if nimi == "":
    print("Kysely lopetettu.")
    print()
    print("Kaikki nimet:")

for nimi in nimet:
    print(f"{nimi}")