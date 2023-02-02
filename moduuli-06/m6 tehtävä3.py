#6.3
print()
print("tehtävä 3")
print()

# funktio saa parametrinaan bensiinin määrän yhdysvaltain nestegallonoina
# funktio palauttaa palauuarvonaan vastaavan litramäärän
# pääohjelma kysyy gallonamäärän ja muuntaa litroiksi
# jatketaan, kunnes käyttäjä syöttää negatiivisen gallonamäärän
# yksi gallona on 3,785 litraa


gallonat = float(input("Anna bensiinin määrä gallonoina: "))
print("Negatiivinen määrä lopettaa toiminnot.")
print()

def muunnos(gallonat):
    litrat = gallonat * 3.785
    return litrat

result = muunnos(gallonat)

while result > 0:
    print(f"{gallonat} gallonaa litroina on: {result} litraa.")
    print()
    gallonat = float(input("Anna bensiinin määrä gallonoina: "))
    result = muunnos(gallonat)

print("Ohjelman suoritus loppui.")