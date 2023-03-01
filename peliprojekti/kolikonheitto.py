


import random

kolikko = random.choice(["Kruuna", "Klaava"])
def coinflip():

    kolikonheitto_satunnainen = "Kruuna" if random.randint(0, 1) > 0.5 else "Klaava"


    import time

    for aika in range(3, 0, -1):
        print(aika)
        time.sleep(1)

    print(kolikonheitto_satunnainen)


    if kolikko == kolikonheitto_satunnainen:
        print("VOITIT!")
    else:
        print("R.I.P")

def random_event():
    sattuma = random.randint(0, 9)
    if sattuma >= 5:
        print("Lentokoneesi on syöksylaskussa!")
        print()
        print(f'Teitä on enää kaksi lentokoneessa, mutta tarjolla on vain yksi laskuvarjo.')
        print(f'Päätätte selvittää kolikonheitolla, kumpi teistä selviää.')
        print(f'Jos kolikko laskeutuu {kolikko} puoli ylöspäin, selviät.')
        print()
        input("Paina 'Enter' jatkaaksesi")
        print(coinflip())
    else:
        print("Selvisit säikähdyksellä!")

print(random_event())
