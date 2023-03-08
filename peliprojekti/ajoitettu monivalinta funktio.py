
import time


def QuestionA(tehtävänanto, vaihtoehto1, vaihtoehto2,vaihtoehto3, aika):
    print()
    print(tehtävänanto)
    print("Painamalla Enter kesken vastaamisen näät kuluneen ajan.")
    start = input("Sinulla on 20 sekuntia aikaa, paina Enter aloittaaksesi: ")
    start_time = time.time()
    points = 4

    # vaihtoehdot tulostuu, jos vastauskenttä on tyhjä
    if start == "":
        print()
        print(f"Vaihtoehto A: {vaihtoehto1}")
        print(f"Vaihtoehto B: {vaihtoehto2}")
        print(f"Vaihtoehto C: {vaihtoehto3}")

    # tehtävä jatkuu, kun vastauskenttä on tyhjä
    while start == "":
        print()
        answer = input("Vastauksesi: ")

        # käyttäjä voi vastata ison tai pienen kirjaimen
        # väärästä vastauksesta lähtee 2 pistettä
        # oikea vastaus tulostaa lopullisen vastausajan ja lopettaa while-loopin

        if answer == "A" or answer == "a":
            print("Oikein!")
            end_time = time.time()
            endtime = end_time - start_time
            print(f"Aikasi oli {round(endtime)} sekuntia.")
            start = "stop"
        elif answer == "B" or answer == "b":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "C" or answer == "c":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "":
            print("")

        # jos käyttäjä ei vastaa mitään vaihtoehdoista, pisteet ei vähene
        else:
            print("Invalid syntax, yritä uudestaan.")

        # jos pisteet menee nolliin, vastausyritykset loppuu
        if points == 0:
            endtime = 20
            print("Yrityksesi loppuivat.")
            start = stop

        # tehtävä loppuu ja pisteet nollautuu, jos vastaamisessa menee yli 20 sekuntia
        now = time.time()
        timer = now - start_time
        if timer >= aika:
            print("Aika loppui :(")
            points = 0
            endtime = 20
            start = stop

        # kulunut aika tulostuu, jos käyttäjä ei ole vielä antanut oikeaa vastausta
        if answer != "A" and answer != "a":
            print(f"Aikaa kulunut {round(timer)} sekuntia.")

    if start != "" and start != "stop":
        points = 0
        endtime = 20

    print()
    print(f"Sait {points} pistettä ja aikaa lennolla on kulunut {round(endtime)} tuntia.")
    return points, round(endtime)


def QuestionB(tehtävänanto, vaihtoehto1, vaihtoehto2,vaihtoehto3, aika):
    print()
    print(tehtävänanto)
    print("Painamalla Enter kesken vastaamisen näät kuluneen ajan.")
    start = input("Sinulla on 20 sekuntia aikaa, paina Enter aloittaaksesi: ")
    start_time = time.time()
    points = 4

    # vaihtoehdot tulostuu, jos vastauskenttä on tyhjä
    if start == "":
        print()
        print(f"Vaihtoehto A: {vaihtoehto1}")
        print(f"Vaihtoehto B: {vaihtoehto2}")
        print(f"Vaihtoehto C: {vaihtoehto3}")

    # tehtävä jatkuu, kun vastauskenttä on tyhjä
    while start == "":
        print()
        answer = input("Vastauksesi: ")

        # käyttäjä voi vastata ison tai pienen kirjaimen
        # väärästä vastauksesta lähtee 2 pistettä
        # oikea vastaus tulostaa lopullisen vastausajan ja lopettaa while-loopin

        if answer == "A" or answer == "a":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "B" or answer == "b":
            print("Oikein!")
            end_time = time.time()
            endtime = (end_time - start_time)
            print(f"Aikasi oli {round(endtime)} sekuntia.")
            start = "stop"
        elif answer == "C" or answer == "c":
            print("Väärin :( yritä uudestaan.")
            points -= 2

        elif answer == "":
            print("")
        # jos käyttäjä ei vastaa mitään vaihtoehdoista, pisteet ei vähene
        else:
            print("Invalid syntax, yritä uudestaan.")

        # jos pisteet menee nolliin, vastausyritykset loppuu
        if points == 0:
            endtime = 20
            print("Yrityksesi loppuivat.")
            break

        # tehtävä loppuu ja pisteet nollautuu, jos vastaamisessa menee yli 20 sekuntia
        now = time.time()
        timer = now - start_time
        if timer >= aika:
            print("Aika loppui :(")
            points = 0
            endtime = 20
            break

        # kulunut aika tulostuu, jos käyttäjä ei ole vielä antanut oikeaa vastausta
        if answer != "B" and answer != "b":
            print(f"Aikaa kulunut {round(timer)} sekuntia.")

    if start != "" and start != "stop":
        points = 0
        endtime = 20

    print()
    print(f"Sait {points} pistettä ja aikaa lennolla on kulunut {round(endtime)} tuntia.")
    return points, round(endtime)


def QuestionC(tehtävänanto, vaihtoehto1, vaihtoehto2,vaihtoehto3, aika):
    print()
    print(tehtävänanto)
    print("Painamalla Enter kesken vastaamisen näät kuluneen ajan.")
    start = input("Sinulla on 20 sekuntia aikaa, paina Enter aloittaaksesi: ")
    start_time = time.time()
    points = 4

    # vaihtoehdot tulostuu, jos vastauskenttä on tyhjä
    if start == "":
        print()
        print(f"Vaihtoehto A: {vaihtoehto1}")
        print(f"Vaihtoehto B: {vaihtoehto2}")
        print(f"Vaihtoehto C: {vaihtoehto3}")

    # tehtävä jatkuu, kun vastauskenttä on tyhjä
    while start == "":
        print()
        answer = input("Vastauksesi: ")

        # käyttäjä voi vastata ison tai pienen kirjaimen
        # väärästä vastauksesta lähtee 2 pistettä
        # oikea vastaus tulostaa lopullisen vastausajan ja lopettaa while-loopin

        if answer == "A" or answer == "a":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "B" or answer == "b":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "C" or answer == "c":
            print("Oikein!")
            end_time = time.time()
            endtime = end_time - start_time
            print(f"Aikasi oli {round(endtime)} sekuntia.")
            start = "stop"

        elif answer == "":
            print("")
        # jos käyttäjä ei vastaa mitään vaihtoehdoista, pisteet ei vähene
        else:
            print("Invalid syntax, yritä uudestaan.")

        # jos pisteet menee nolliin, vastausyritykset loppuu
        if points == 0:
            endtime = 20
            print("Yrityksesi loppuivat.")
            break

        # tehtävä loppuu ja pisteet nollautuu, jos vastaamisessa menee yli 20 sekuntia
        now = time.time()
        timer = now - start_time
        if timer >= aika:
            print("Aika loppui :(")
            points = 0
            endtime = 20
            break

        # kulunut aika tulostuu, jos käyttäjä ei ole vielä antanut oikeaa vastausta
        if answer != "C" and answer != "c":
            print(f"Aikaa kulunut {round(timer)} sekuntia.")

    if start != "" and start != "stop":
        points = 0
        endtime = 20

    print()
    print(f"Sait {points} pistettä ja aikaa lennolla on kulunut {round(endtime)} tuntia.")
    return points, round(endtime)


# -- pääohjelma --------------------------------------------------------------------------------------------------------

# luodaan tyhjä lista ja kokonaispistemäärä
kokonaispisteet_lista = []
kokonaispisteet_summa = 0
aikaakulunut = 0

# haetaan funktion palauttama arvo ja lisätään se listalle
result = QuestionA("tehtävänanto", "vaihtoehto1", "vaihtoehto2", "vaihtoehto3", 20)
result = kokonaispisteet_lista.append(result)

result = QuestionB("tehtävänanto", "vaihtoehto1", "vaihtoehto2", "vaihtoehto3", 20)
result = kokonaispisteet_lista.append(result)

result = QuestionC("tehtävänanto", "vaihtoehto1", "vaihtoehto2", "vaihtoehto3", 20)
result = kokonaispisteet_lista.append(result)


# varmistusprinttaus
print(kokonaispisteet_lista)

# lisätään saadut pisteet kokonaispistemäärään
for a in kokonaispisteet_lista:
    kokonaispisteet_summa += a[0]
print(f"Kokonaispisteesi on {kokonaispisteet_summa}.")

# lisätään kulunut aika kokonaismäärään
for a in kokonaispisteet_lista:
    aikaakulunut += a[1]
print(f"Aikaa on kulunut {aikaakulunut} tuntia.")