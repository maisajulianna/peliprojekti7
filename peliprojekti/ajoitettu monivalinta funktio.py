
import time

# kolmen vaihtoehdon monivalitatehtävä, jossa oikea vastaus on c-kohta
def QuestionC(vaihtoehto1, vaihtoehto2,vaihtoehto3,):
    print()
    print("Kysymys 1:")
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
            print(f"Aikasi oli {round(end_time - start_time)} sekuntia.")
            start = "stop"

        elif answer == "":
            print("")
        # jos käyttäjä ei vastaa mitään vaihtoehdoista, pisteet ei vähene
        else:
            print("Invalid syntax, yritä uudestaan.")

        # jos pisteet menee nolliin, vastausyritykset loppuu
        if points == 0:
            print("Yrityksesi loppuivat.")
            break

        # tehtävä loppuu ja pisteet nollautuu, jos vastaamisessa menee yli 20 sekuntia
        now = time.time()
        timer = now - start_time
        if timer >= 20:
            print("Aika loppui :(")
            points = 0
            break

        # kulunut aika tulostuu, jos käyttäjä ei ole vielä antanut oikeaa vastausta
        if answer != "C" and answer != "c":
            print(f"Aikaa kulunut {round(timer)} sekuntia.")

        end_time = time.time()

    if start != "" and start != "stop":
        points = 0

    print()
    print(f"Sait {points} pistettä")


QuestionC("joo", "ei", "idk")