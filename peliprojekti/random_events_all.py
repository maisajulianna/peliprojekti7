
import random
import time

kolikko = random.choice(["Kruuna", "Klaava"])
def coinflip():

    kolikonheitto_satunnainen = "Kruuna" if random.randint(0, 1) > 0.5 else "Klaava"

    import time

    for aika in range(3, 0, -1):
        print(aika)
        time.sleep(1)

    print(kolikonheitto_satunnainen)

    if kolikko == kolikonheitto_satunnainen:
        print("Selvisit. Laskeudut turvallisesti seuraavalle lentokentälle")
    else:
        print("R.I.P")
    return

def random_event_1():
        print("Lentokoneesi on syöksylaskussa!")
        print(f'Teitä on enää kaksi lentokoneessa, mutta tarjolla on vain yksi laskuvarjo.')
        print(f'Päätätte selvittää kolikonheitolla, kumpi teistä selviää.')
        print(f'Jos kolikko laskeutuu {kolikko} puoli ylöspäin, selviät.')
        print()
        input("Paina 'Enter' jatkaaksesi")
        coinflip()
        return

def lottokone():
    print("Löydät lottolipun maasta")
    print("Syötä lappuun kaksi arpanumeroa ja yritä lunastusta läheiseltä kioskilta")
    print()
    voittonumerot = random.sample(range(1, 11), 2)
    pelaaja_numerot = []
    for i in range(2):
        while True:
            try:
                numero = int(input("Syötä numero väliltä 1-10: "))
                if numero < 1 or numero > 10:
                    raise ValueError
                break
            except ValueError:
                print("Virhe. Syötä numero väliltä 1-10: ")
        pelaaja_numerot.append(numero)

    if pelaaja_numerot == voittonumerot:
        print("Onnittelut! Voitit 10 pistettä!")
    else:
        print(f'Valitettavasti arpaonni ei suosinut tällä kertaa, voittonumerot: {voittonumerot}')
        return

def random_event_conversation():
    vastaus_a = "Jatka kohti vessaa"
    vastaus_b = "Pahoittele ja anna 2 pistettä"

    print("Etenet lentokoneessa kohti vessaa, matkallasi tönäiset kuitenkin vihaisen oloista mieshenkilöä.")
    print("Mies kääntää päänsä ja vaikuttaa nyt hyvin vihaiselta.")
    print()
    print("Miten etenet?")
    print(f'A: {vastaus_a}')
    print(f'B: {vastaus_b}')

    vaihtoehdot = ["a", "b"]
    toiminta = True

    while toiminta:
        print()
        pelaaja = input("Vastauksesi: ").lower()
        print()

        if pelaaja not in vaihtoehdot:
            print("Virhe. Yritä uudelleen.")
            print()

        else:
            if pelaaja == "a":
                print("Mieshenkilö ei vaikutakaan enää kovin vihaiselta ja haluaa tarjota sinulle kaksi vaihtoehtoa:")
                print()
                print("A: Jatka matkaasi vessaan")
                print("B: Ota huikka miehen vihreästä pullosta")
                vaihtoehdot = ["a", "b"]
                print()
                valinta = input("Vastauksesi: ").lower()
                if valinta == "a":
                    print("'Wrong answer pal...'")
                    print()
                    print("Heräät lentokoneen ensiapuvuoteelta, hoitokulusi ovat 4 pistettä")
                toiminta = False

                if valinta =="b":
                      print("          Otit huikan...")
                      print("...askel vaikuttaa heti keveämmältä...")
                      print()
                      print("Voit jatkaa matkaasi.")
                toiminta = False

            elif pelaaja == "b":
                print("'You got lucky this time, pal...'")
                print()
                print("Selvisit säikähdyksellä, onneksi ei käynyt pahemmin...")
            toiminta = False

def convo_homeless():

        print("Törmäät lentokentän käytävällä kodittomaan henkilöön")
        print("Hän anelee sinulta yhtä pistettä")
        print()
        valinta = input("Annatko pisteen (Kyllä/Ei) ")

        if valinta.lower() == "kyllä" or "k":
            print("Annoit pisteen.")
        if valinta.lower() == "ei" or "e":
            print("Koditon: :-(")

def random_event_click():
    import time

    print("Otat osaa kilpailuun.")
    print("Tehtävänäsi on painaa 'Enter'-näppäintä sata (100) kertaa 15 sekunnin aikana!")
    print()
    print(input("Paina Enter aloittaaksesi:"))

    pisteet = 0
    start_time = time.time()

    while True:
        input(f'Paina Enter {pisteet}/100')
        pisteet += 1
        time_elapsed = time.time() - start_time
        if time_elapsed >= 15:
            break
        if pisteet == 100:
            break

    print("Aika loppui!")
    if pisteet >= 100:
        print(f'Onnea, voitit pisteen! Kulunut aika: {round(time_elapsed, 2)} sekuntia')
    else:
        print(f'Hävisit! Kokonaistulos: {pisteet}')

def robbery_bob_2():

    vastaus_a = "Osta oma lippu (-2p)"
    vastaus_b = "Yritä anastaa lippu"

    print("On aika hankkia liput seuraavaan kohteeseen matkustamiseen.")
    print("Olet matkalla kohti lippupistettä, kunnes huomaat penkillä nukkuvan vanhuksen, jonka taskusta pilkistää lentolippu.")
    print()
    print("Mahdollisuutesi on yrittää anastaa lippu häneltä tai hakea oma kahta pistettä vastaan")
    print()
    print("Miten toimit?")
    print(f'A: {vastaus_a}')
    print(f'B: {vastaus_b}')

    vaihtoehdot = ["a", "b"]
    toiminta = True

    while toiminta:
        print()
        pelaaja = input("Vastauksesi: ").lower()
        print()

        if pelaaja not in vaihtoehdot:
            print("Virhe. Yritä uudelleen.")
            print()

        else:
            if pelaaja == "b":
                print("Kurotat kätesi taskulle...")
                print("Haluatko varmasti jatkaa?")
                print()
                print("A: Anasta lippu")
                print("B: Käänny, ja osta oma lippusi (-2p)")
                vaihtoehdot = ["a", "b"]
                print()
                valinta = input("Vastauksesi: ").lower()
                if valinta == "b":
                    print("Ostit oman lipun ':D'")
                toiminta = False

                if valinta == "a":
                    print("Sait lipun... Pakenet...")
                    print()
                    print("Matkallasi kohti lähtöselvitystä vartija pysäyttää sinut.")
                    print("Turvakameratalleenteesta on selvinnyt, että olet varastanut lipun.")
                    print()
                    print("Rangaistuksesi saat 4 pisteen sakon")

                toiminta = False

            elif pelaaja == "a":
                print("Ostit oman lipun ':D'")
            toiminta = False

def kivipaperisakset():

    print("Sinut haastetaan 'kivi, paperi, sakset' -peliin")
    print("Voit joko voittaa tai hävitä yhden pisteen")
    print()
    print("Syötä valintasi, kun olet valmis aloittamaan")

    vaihtoehdot = ("kivi", "paperi", "sakset")
    toiminta = True

    while toiminta:

        pelaaja = None
        tietokone = random.choice(vaihtoehdot)

        while pelaaja not in vaihtoehdot:
            pelaaja = input("Syötä valinta (kivi, paperi, sakset): ")
            print()

        if pelaaja not in vaihtoehdot:
                print("Virhe. Yritä uudelleen.")
                print()

        print(f'Pelaaja: {pelaaja}')
        print(f'Tietokone: {tietokone}')

        if pelaaja == tietokone:
            print("Tasapeli! Uusintakierros.")
            print()
            return kivipaperisakset()



        elif pelaaja == "kivi" and tietokone == "sakset":
            print("Sinä voitit! (+1p)")

        elif pelaaja == "paperi" and tietokone == "kivi":
            print("Sinä voitit! (+1p)")

        elif pelaaja == "sakset" and tietokone == "paperi":
            print("Sinä voitit! (+1p)")

        else:
            print("Sinä hävisit. (-1p)")
        toiminta = False

def luonnonkatastrofit():
    def turbulenssi():
        skenaariot = [
            "Matkallasi törmäät yllättäen kovaan turbulenssiin. Kone alkaa poukkoilla edestakaisin ja turvavyövalo syttyy...",
        ]

        skenaario = random.choice(skenaariot)
        print(skenaario)

        if random.random() < 0.3:
            print()
            print("Puhelimesi tippui taskusta lennolla turbulenssin aikana. Lunastat uuden lentoasemalta kahdella pisteellä.")

    def myrsky():
        skenaariot = [
            "Pyörremyrsky ottaa koneesi valtaan ja tavarat lentelevät ympäriinsä, toivottavasti kaikki on tallella..."
        ]

        skenaario = random.choice(skenaariot)
        print(skenaario)

        if random.random() < 0.6:
            print()
            print("Rannekellosi on hävinnyt lennolla. Käyt ostamassa lentokentältä uuden kahdella pisteellä")

    def tulivuori():
        skenaariot = [
            "Lentokoneesi joutuu lentämään tulivuoren yli, ja ikkunoista näkyy punaisena hehkuva kraateri..."
        ]

        skenaario = random.choice(skenaariot)
        print(skenaario)

        if random.random() < 0.5:
            print()
            print("Joudut ostamaan uuden matkalaukun, koska se kärsi vaurioita tulivuorelennon aikana. Lunastat kentältä uuden kolmella pisteellä.")

    katastrofi = random.choice([turbulenssi, myrsky, tulivuori])
    katastrofi()


def random_event_all():
    randomizer = random.randint(0, 20)

    if randomizer <=3:
        random_event_1()

    elif (3<randomizer<6):
        lottokone()

    elif (6<randomizer<9):
        random_event_conversation()

    elif (9<randomizer<12):
        convo_homeless()

    elif (12<randomizer<14):
        random_event_click()

    elif (14<randomizer<16):
        robbery_bob_2()

    elif (16<randomizer<18):
        kivipaperisakset()

    elif (18<randomizer<21):
        luonnonkatastrofit()



random_event_all()
