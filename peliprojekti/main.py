import mysql.connector
import time
import sys
import pygame


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user="userN",
    password="1234",
    autocommit=True)


saved = False
kokonaispisteet_lista = []


# funktio näyttää tekstiä peli-ikkunassa
def print_text(screen, message, x, y, font_color=(0,0,0),\
               font_type = "C:/Users/maisa/PycharmProjects/ohjelmisto1/peliprojekti/images/magneto_bold.ttf", font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x,y))
    pygame.display.flip()


# Näytämme pelin tarinan ja lentävän lentokoneen, kunnes käyttäjä napsauttaa ENTER
def welcome():
    pygame.init()
    size = width, height = 600, 600
    speed = [1, 1]                  # lennon kuvan muutos videon aikana
    black = 0, 0, 0
    white = 255, 255, 255
    need_input = False
    screen = pygame.display.set_mode(size)
    logo = pygame.image.load("images/logo_game.png")
    tarina = pygame.image.load("images/tarina.png")
    logo_rect = logo.get_rect()
    tarina_rect = tarina.get_rect()
    logo_rect = logo_rect.move([1,height])
    pygame.display.set_caption("MVMN-Lentopeli")
    show_welcome = True
    while show_welcome:
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    sys.exit()
                 if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    show_welcome = False

            logo_rect = logo_rect.move([1,-1])
            screen.fill(white)
            screen.blit(tarina, tarina_rect)
            screen.blit(logo, logo_rect)
            pygame.display.flip()
            time.sleep(0.01)
    pygame.quit()


#ask user_name
def get_user():
    pygame.init()
    size = width, height = 600, 600
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("MVMN-Lentopeli")
    screen.fill(white)
    pygame.display.flip()
    print_text(screen, "Aloitetaan...", 10, 1)
    print_text(screen, "Anna haluamasi käyttäjänimi: ", 10, 30)
    need_input = True
    user_name = ''
    while need_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if need_input and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        need_input = False

                    elif event.key == pygame.K_BACKSPACE:
                        user_name = user_name[0:-1]
                        screen.fill(white)
                        print_text(screen, "Aloitetaan...", 10, 1)
                        print_text(screen, "Anna haluamasi käyttäjänimi: ", 10, 30)
                        pygame.display.flip()
                        print_text(screen, user_name, 350, 30)

                    elif len(user_name) < 20:
                        user_name = user_name + event.unicode
                        print_text(screen, user_name, 350, 30)

    print_text(screen, "Hei, " + user_name + "!", 10, 90)
    time.sleep(3)
    #check if user_name already exists in the table game (not finished games)

    sql = "select * from game where screen_name = '" + user_name + "';"

    kursori = connection.cursor()
    kursori.execute(sql)
    result = kursori.fetchone()

    if not result:  #Jos tietokannassa ei ole samannimistä käyttäjää
        print_text (screen, user_name + ", sinulla ei ole keskeneräisiä pelejä.", 10, 120)
        print_text(screen, "Aloitetaan uusi peli hetken kuluttua...", 10, 150)
        # add user to DB
        sql = "insert into game values (NULL, 0,'" + user_name + "',"\
              " 0, NULL, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)"
        kursori.execute(sql)
        sql = "select * from game where screen_name = '" + user_name + "';"
        kursori.execute(sql)
        user = kursori.fetchone()    # user - kaikki tiedot nykyisestä pelaajasta
        need_input = False
        time.sleep(3)
        pygame.quit()

    else: #Jos tietokannassa on samannimistä käyttäjää
        print_text(screen, "Olet jo aloittanut pelaamisen, haluatko jatkaa?", 10, 120)
        print_text(screen, "a - jatka viimeistä peliä", 10, 150)
        print_text(screen, "b - aloita uusi peli ja poista vanhan pelin tulokset", 10, 180)
        print_text(screen, "c - vaihda käyttäjänimi", 10, 210)
        need_input = True
        while need_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if need_input and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                       print_text(screen, "a", 10, 240)
                       time.sleep (3)
                       user = result               # user - kaikki tiedot nykyisestä pelaajasta
                       need_input = False
                       connection.close()
                    if event.key == pygame.K_b:    # "vanha" pelaaja aloittaa uuden pelin -
                                                   # on poistettava kaikki tiedot edellisestä pelistä
                        print_text(screen, "b", 10, 240)
                        sql = "update game set AF_= FALSE, AN_ = FALSE, AS_ = FALSE, " + \
                              "EU_= FALSE, NA_ = FALSE, OC_= FALSE,SA_ = FALSE, time_sec = 0, " + \
                              "score = 0, last_location = NULL where player_id=" + str(result[0])
                        kursori.execute(sql)
                        sql = "select * from game where player_id=" + str(result[0])
                        kursori.execute(sql)
                        user = kursori.fetchone() # user - kaikki tiedot nykyisestä pelaajasta
                        connection.close()
                        need_input = False
                        time.sleep(3)
                    if event.key == pygame.K_c:
                        print_text(screen, "c", 10, 240)
                        need_input = False
                        connection.close()
                        pygame.quit()
                        user = get_user()  # Varoitus, rekursio!
    return user


def delete_game(user):
    # delete current game of this user
    kursori = connection.cursor()

    sql = "delete from game where player_id=" + str(user[0])+ ";"
    kursori.execute(sql)
    connection.close()


def timer(s):
    for aika in range(s, 0, -1):
        print(aika)
        time.sleep(1)
    print("Aika loppui!")


def timenoprint(s):
    for aika in range(s, 0, -1):
        # print(aika)
        time.sleep(1)
    # print("Aika loppui!")


def peliohjeet():
    print()
    print("Lentomatkan varrella sinulta kysytään kysymyksiä matkakohteesta.")
    print("Kysymykset ovat kolmen kohdan monivalintakysymyksiä.")
    print("Yhdestä tehtävästä voit saada 4 pistettä. Jos vastaat väärin, maximi pistemäärä laskee 2 pisteellä.")
    print("Tehtävä loppuu, jos pisteet laskevat nolliin.")
    print()
    print("Tehtävissä on aika, joka mittaa lentomatkasi pituutta.")
    print("Jos annettu aika ylittyy ennen kuin vastaat oikein, saat 0 pistettä.")
    print("Onnea vastaamiseen!")
    print()


def options():
    loop = True
    while loop == True:
        print()
        print("1: Vaihda lentokone")
        # print("2: Tallenna tämänhetkiset tiedot")
        print("3: Poista aikaisemmat tiedot")
        print("4: Näytä peliohjeet uudestaan")
        print()
        choice = int(input("Mitä haluaisit tehdä? "))
        if choice == 1:
            plane = choose_plane()
            return plane
        elif choice == 2:
            saved = save_result()
            print(f"Tallennettu tietoja nimellä {saved[0]}: {saved[1]} pistettä, {saved[2]} tuntia, paikassa {saved[3]}")
        elif choice == 3:
            delete_game(user)
        elif choise == 4:
            peliohjeet()
        else:
            print()
            print("Virheellinen arvo.")
            loop = int(input("Paina 1 jos haluat jatkaa valitsemista, 2 jos haluat lopettaa. "))
            if loop == "1":
                loop = True
            elif loop == "2":
                print("Prosessi lopetettu.")
                loop = False


def choose_options():
    print()
    option = input("(Paina kirjainta V jos haluat nähdä vaihtoehdot.) ")
    if option == "v" or option == "V":
        options()


def choose_plane():
    # while loop jotta halutessaan vaihtoehdot saa uudestaan näkyviin

    sql = f"SELECT type FROM plane_info"
    cursor = connection.cursor()
    cursor.execute(sql)
    planes = cursor.fetchall()
    sql = f"SELECT id, emission, risk, questions, velocity FROM plane_info"
    cursor = connection.cursor()
    cursor.execute(sql)
    info = cursor.fetchall()
    print()
    print("Aloitetaan valitsemalla lentokone.")
    print()
    print("Minkä lentokoneen haluaisit valita?")
    print("Vaihtoehdot:")

    chosen = False
    while chosen == False:
        chosen = True
        times = 0
        for i in info:
            plane = info[times]
            type = planes[times]
            print(f"{plane[0]}: Koneen {type[0]} päästötaso on {plane[1]}, riskitaso {plane[2]}" \
                  f" ja nopeus {plane[3]}. Kysymyksiä matkalla on {plane[4]}.")
            times += 1

        print()
        plane = 0
        planeNumber = int(input("Valitsemasi lentokoneen numero: "))
        if planeNumber == 1:
            plane = planes[0]
            plane = plane[0]
            print(f"Valitsemasi lentokone on {plane}.")
        elif planeNumber == 2:
            plane = planes[1]
            plane = plane[0]
            print(f"Valitsemasi lentokone on {plane}.")
        elif planeNumber == 3:
            plane = planes[2]
            plane = plane[0]
            print(f"Valitsemasi lentokone on {plane}.")
        elif planeNumber == 4:
            plane = planes[3]
            plane = plane[0]
            print(f"Valitsemasi lentokone on {plane}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vaan numeroa jos haluat lopettaa.")
            again = int(input("Paina 1, jos haluat valita uudestaan: "))
            print()
            if again == 1:
                print()
                print("Vaihdoehdot uudestaan:")
                chosen = False
            else:
                print("Lopetit pelin.")

        if planeNumber >= 1 and planeNumber <=4 :
            print()
            confirmation = input("Oletko tyytyväinen valintaasi? Varmista painamalla Enter. ")
            if confirmation == "":
                print("Lentokone valittu!")
                chosen = True
            else:
                print()
                print("Valitse uudestaan:")
                chosen = False
    return planeNumber, plane


def choose_start():
    print("Seuraavaksi saat valita lentokentän, jolta aloitat pelin.")
    # sql =
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    times = 0
    print("Lentokenttävaihtoehdot:")
    print()
    for result in result:
        byname = result[times]
        print(f"Lentokenttä {byname[0]} maassa {byname[1]}.")
        times = times + 1
    print(result)


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


kokonaispisteet_summa = 0
aikaakulunut = 0

def pistelaskuri():
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
    return kokonaispisteet_summa, aikaakulunut


def end():
    pygame.init()
    size = width, height = 600, 600
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("MVMN-Lentopeli")
    screen.fill(white)
    pygame.display.flip()

    #lentava lentokone
    logo = pygame.image.load("images/logo_game.png")
    logo_rect = logo.get_rect()
    logo_rect = logo_rect.move([1, height])
    flight = True
    x = 50
    y = height - 50
    while x < width-50:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        logo_rect.centerx = x
        y = 0.005*(x**2)-3.3*x+700
        logo_rect.centery = y

        screen.fill(white)
        screen.blit(logo, logo_rect)
        pygame.display.flip()
        x += 1
        time.sleep(0.01)

    # show all results from table results
    kursori = connection.cursor()
    sql = "select * from results;"
    kursori.execute(sql)
    tulokset = kursori.fetchall()
    print_text(screen, "TULOKSET", 250, 20)
    print_text(screen, "Nimi", 60, 80)
    print_text(screen, "Pisteet", 260, 80)
    print_text(screen, "Aika", 360, 80)
    rivi = 130
    for t in tulokset:
        print_text(screen, str(t[1]), 60, rivi)
        print_text(screen, str(t[2]), 260, rivi)
        print_text(screen, str(t[3]), 360, rivi)
        rivi += 40

    time.sleep(5)


# -- pääohjelma ---------------------------------------------------------------------------------------------

# pelaajan nimen valinta ja pelaajanumeron luominen

welcome()
user = get_user()

timenoprint(1)

# lentokoneen ja lähtöpaikan valinta
plane = choose_plane()
# start = choose_airport()


peliohjeet()

# tehtäviä
result = QuestionA("tehtävänanto", "vaihtoehto1", "vaihtoehto2", "vaihtoehto3", 20)
result = kokonaispisteet_lista.append(result)

result = QuestionB("tehtävänanto", "vaihtoehto1", "vaihtoehto2", "vaihtoehto3", 20)
result = kokonaispisteet_lista.append(result)

result = QuestionC("tehtävänanto", "vaihtoehto1", "vaihtoehto2", "vaihtoehto3", 20)
result = kokonaispisteet_lista.append(result)

# tehtävien pisteet
result = pistelaskuri()
kokonaispisteet_summa = result[0]
aikaakulunut = result[1]


choose_options()
save_result(user, aikaakulunut, kokonaispisteet_summa, airport)

choose_options()


# game over screen
# end()
