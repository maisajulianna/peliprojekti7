#5.3
print()
print("tehtävä 3")
print()

# kysy käyttäjältä kokonaisluku
# ilmoita onko se alkuluku
# alkuluvut ovat jaollisia vain 1 ja itsellään

lista = []
total = 0
luku = int(input("Anna luku: "))

alkuluku = True

for i in range(2,luku):
    if luku % i == 0:
        print(f"Luku {luku} ei ole alkuluku.")
        alkuluku = False
        break

if alkuluku == True:
    print(f"Luku {luku} on alkuluku.")
