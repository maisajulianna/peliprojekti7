import mysql.connector
import time
import sys
import pygame
import random


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user="userN",
    password="1234",
    autocommit=True)



# --- --- alkujuttuja
def print_text(screen, message, x, y, font_color=(0,0,0),\
               font_type = "C:/Users/maisa/PycharmProjects/ohjelmisto1/peliprojekti/images/magneto_bold.ttf", font_size=20):

    # funktio näyttää tekstiä peli-ikkunassa
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x,y))
    pygame.display.flip()

def welcome():
    # Näytämme pelin tarinan ja lentävän lentokoneen, kunnes käyttäjä napsauttaa ENTER
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
            # time.sleep(0.01)
    pygame.quit()


def get_user():
    # ask user_name
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
    # time.sleep(3)
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
        # time.sleep(3)
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
                       # time.sleep (3)
                       user = result               # user - kaikki tiedot nykyisestä pelaajasta
                       need_input = False
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
                        need_input = False
                        time.sleep(3)
                    if event.key == pygame.K_c:
                        print_text(screen, "c", 10, 240)
                        need_input = False
                        user = get_user()  # Varoitus, rekursio!
    pygame.quit()
    return user


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



# --- --- satunnaisia funktioita
def delete_game(user):
    # delete current game of this user
    kursori = connection.cursor()

    sql = "delete from game where player_id=" + str(user[0])+ ";"
    kursori.execute(sql)


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


def continent_name(continent_abbr):
    if continent_abbr == 'AF':
        continent_fi = "Afrikka"
    elif continent_abbr == 'EU':
        continent_fi = "Eurooppa"
    elif continent_abbr == 'NA':
        continent_fi = "Pohjois-Amerikka"
    elif continent_abbr == 'SA':
        continent_fi = "Etelä-Amerikka"
    elif continent_abbr == 'OC':
        continent_fi = "Australia ja Oseania"
    elif continent_abbr == 'AS':
        continent_fi = "Aasia"
    elif continent_abbr == 'AN':
        continent_fi = "Antarctica"
    return continent_fi



# --- --- aloitusvalintoja
def choose_plane():

    sql = f"SELECT type, id, emission, risk, questions, velocity FROM plane_info"
    cursor = connection.cursor()
    cursor.execute(sql)
    planes = cursor.fetchall()
    print()
    print("Aloitetaan valitsemalla lentokone.")
    print()
    print("Minkä lentokoneen haluaisit valita?")
    print("Vaihtoehdot:")

    times = 0
    for i in planes:
        plane = planes[times]
        print(f"{plane[1]}: Koneen {plane[0]} päästötaso on {plane[2]}, riskitaso {plane[3]} prosenttia" \
              f" ja nopeus {plane[5]}. Kysymyksiä matkalla on {plane[4]}.")
        times += 1

    chosen = False
    while chosen == False:
        chosen = True

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
            print("Paina mitä vain, jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan: ")
            print()
            if again == "":
                chosen = False
            else:
                print("Lopetit pelin.")

        if planeNumber >= 1 and planeNumber <=4 :
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Lentokone valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT type, id, emission, risk, questions, velocity FROM plane_info"
                cursor = connection.cursor()
                cursor.execute(sql)
                planes = cursor.fetchall()
    return planeNumber, plane


def choose_start():
    sql = f"SELECT ident, name, municipality, iso_country, continent FROM airport " \
          f"WHERE ident = 'DNMM' OR ident = 'ZBAA' OR ident = 'EDDF' " \
          f"OR ident = 'KLAS' OR ident = 'YSSY' OR ident = 'SBJH'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    # print(airports)
    print()
    print("Seuraavaksi saat valita lentokentän, jolta aloitat pelin.")
    print()
    print("Lentokenttävaihtoehdot:")
    print()

    print('%-47s %-27s %-10s %-10s' % ("Lentokentän nimi:", "Kunta:", "Maa:", "Maanosa:"))
    times = 0
    id = 1
    for i in airports:
        airport = airports[times]
        print('%-4d %-45s %-25s %-10s %-10s' % (id, airport[1], airport[2], airport[3], airport[4]))
        times += 1
        id += 1

    chosen = False
    while chosen == False:
        chosen = True

        print()
        airport_id = int(input("Valitsemasi lentokentän numero: "))
        airport = 0

        if airport_id >= 1 and airport_id <= 6:
            index = airport_id - 1
            airport = airports[index][1]
            continent_abbr = airports[index][4]
            continent = continent_name(continent_abbr)
            print(f"Olet lentokentällä {airport} maanosassa {continent}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain, jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan: ")
            print()
            if again == "":
                chosen = False
            else:
                print("Lopetit pelin.")

        if airport_id >= 1 and airport_id <= 6:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Lentokenttä valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT ident, name, municipality, iso_country, continent FROM airport " \
                      f"WHERE ident = 'DNMM' OR ident = 'ZBAA' OR ident = 'EDDF' " \
                      f"OR ident = 'KLAS' OR ident = 'YSSY' OR ident = 'SBJH'"
                cursor = connection.cursor()
                cursor.execute(sql)
                airports = cursor.fetchall()
    return airport, continent_abbr



# --- --- matkakohdefunktiot
def choose_continent(from_continent):
    sql = f"SELECT continent FROM airport GROUP BY continent"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    continents = cursor.fetchall()
    # print(continents)

    print()
    print("Mihin haluat lentää?")
    print()
    print("Valitse aluksi maanosa: ")

    times = 0
    id = 1
    for i in continents:
        one = continents[times]
        continent_abbr = one[0]
        continenT = continent_name(continent_abbr)
        print(f"{id}: {continenT}")
        if continent_abbr == from_continent:
            print("(Olet jo täällä!)")
        times += 1
        id += 1

    chosen = False
    while chosen == False:
        gameover1 = False
        print()
        continentNro = int(input("Haluamasi maanosan numero: "))
        to_continent = 0

        if continentNro >= 1 and continentNro <= 7:
            index = continentNro - 1
            continents = continents[index]
            to_continent = continents[0]
            continent = continent_name(to_continent)
            print(f"Valitsemasi maanosa on {continent}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan. ")
            if again == "":
                chosen = False
            else:
                print()
                print("Lopetit pelin.")
                chosen = True
                gameover1 = True

        if continentNro >= 1 and continentNro <=7 :
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Maanosa valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT continent FROM airport GROUP BY continent"
                cursor = connection.cursor()
                cursor.execute(sql)
                continents = cursor.fetchall()
    return to_continent, gameover1


def choose_country(to_continent):
    #print(to_continent)
    print()
    print("Valitse seuraavaksi maa.")
    print()
    print("Valitsemasi maanosan maat:")

    sql = f"SELECT name, iso_country FROM country WHERE continent = '{to_continent}' GROUP BY name"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    countries = cursor.fetchall()
    # print(countries)

    times = 0
    id = 1
    for i in countries:
        one = countries[times]
        country = one[0]
        print(f"{id}: {country}")
        times += 1
        id += 1

    chosen = False
    while chosen == False:
        gameover2 = False
        print()
        list_index = len(countries)
        countryNro = int(input("Haluamasi maan numero: "))
        to_country = 0
        # print(list_index)

        if countryNro >= 1 and countryNro <= list_index:
            index = countryNro - 1
            countries = countries[index]
            to_country = countries[0]
            iso_country = countries[1]
            print(f"Valitsemasi maa on {to_country}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain, jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan: ")
            print()
            if again == "":
                chosen = False
            else:
                print("Lopetit pelin.")
                chosen = True
                gameover2 = True

        if countryNro >= 1 and countryNro <= list_index:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Maa valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT iso_country FROM airport WHERE continent = '{to_continent}' GROUP BY iso_country"
                cursor = connection.cursor()
                cursor.execute(sql)
                countries = cursor.fetchall()
    return iso_country, gameover2


def choose_airport(to_country):
    print()
    print("Valitse vielä lentokenttä.")
    print()
    print("Lentokentät valitsemassasi kaupungissa:")

    sql = f"SELECT name, ident, municipality FROM airport WHERE iso_country = '{to_country}'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    airports_list = cursor.fetchall()
    # print(airports_list)
    print()

    print('%-40s %-40s' % ("Lentokentän nimi:", "Sijainti:"))
    times = 0
    id = 1
    for i in airports_list:
        airport_name = airports_list[times][0]
        airport_place = airports_list[times][2]
        print('%-5d %-40s %-40s' % (id, airport_name, airport_place))
        id += 1
        times += 1

    gameover3 = False
    chosen = False
    continue_game = False

    while chosen == False:

        print()
        list_index = len(airports_list)
        # print(list_index)
        airportNro = int(input("Haluamasi lentokentän numero: "))
        airport = 0

        if airportNro >= 1 and airportNro <= list_index:
            index = airportNro - 1
            airports_list = airports_list[index]
            airport = airports_list[0]
            airport_ident = airports_list[1]
            print(f"Valitsemasi lentokenttä on {airport}.")
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
                gameover3 = True

        if airportNro >= 1:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter.")
            if confirmation == "":
                print("Lentokenttä valittu!")
                chosen = True
                continue_game = True
            else:
                chosen = False
                sql = f"SELECT name, ident, municipality FROM airport WHERE iso_country = '{to_country}'"
                cursor = connection.cursor()
                cursor.execute(sql)
                airports_list = cursor.fetchall()
    return airport, airport_ident, gameover3, continue_game


def travel():
    gameover_main = False
    while gameover_main == False:

        result = choose_continent(start_continent)
        to_continent = result[0]
        gameover_main = result[1]
        if gameover_main == True:
            break

        result = choose_country(to_continent)
        to_country = result[0]
        gameover_main = result[1]
        if gameover_main == True:
            break

        result = choose_airport(to_country)
        to_airport = result[0]
        airport_ident = result[1]
        gameover_main = result[2]
        continue_game1 = result[3]
        if gameover_main == True:
            break

        if continue_game1 == True:
            break

    return to_airport, airport_ident, to_continent, gameover_main



# --- ---  kysymysfunktiot
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


def pistelaskuri(kokonaispisteet_lista):
    # varmistusprinttaus
    # print(f"Kokonaispistelista funktiossa {kokonaispisteet_lista}")
    print()

    # funktion oma muuttuja ('yhteispisteet')
    yhteispisteet = kokonaispisteet_summa

    # lisätään saadut pisteet kokonaispistemäärään
    for a in kokonaispisteet_lista:
        yhteispisteet += a[0]
    print(f"Sinulla on tällä hetkellä {yhteispisteet} pistettä.")

    # funktion sisäinen muuttuja 'yhteisaika'
    yhteisaika = aikaakulunut

    # lisätään kulunut aika kokonaismäärään
    for a in kokonaispisteet_lista:
        yhteisaika += a[1]
    print(f"Aikaa on kulunut {yhteisaika} tuntia.")
    return yhteispisteet, yhteisaika


def travel_questionsAF(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = '{planeNumber}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")
    input("Paina Enter jatkaaksesi. ")

    rip = False
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionA("Montaako kieltä Afrikassa puhutaan?", "Yli 2000", "Noin 1300", "830", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Missä Afrikan maassa on eniten pyramideja?", "Egyptissä", "Libyassa", "Sudanissa", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionB("Milloin Etiopiassa juhlitaan uutta vuotta?", "1.1.", "11.9.", "24.5.", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionA("Mikä on Afrikan pinta-ala?", "30 365 000 neliökilometriä", "21 222 421 neliökilometriä", "18 032 341 neliökilometriä", 20)
        kokonaispisteet_lista.append(result4)
        rip = incident_risk1(1)
    elif planeNumber == 3:
        result1 = QuestionC("Missä Afrikan maassa on eniten pyramideja?", "Egyptissä", "Libyassa", "Sudanissa", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionA("Montaako kieltä Afrikassa puhutaan?", "Yli 2000", "Noin 1300", "830", 20)
        kokonaispisteet_lista.append(result2)
        rip = incident_risk1(2)
    elif planeNumber == 4:
        result1 = QuestionB("Milloin Etiopiassa juhlitaan uutta vuotta?", "1.1.", "11.9.", "24.5.", 20)
        kokonaispisteet_lista.append(result1)
        rip = incident_risk1(3)
    return kokonaispisteet_lista, rip


def travel_questionsAN(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = '{planeNumber}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")
    input("Paina Enter jatkaaksesi. ")

    play_points = 0
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionB("Paljonko on Etelämantereen mannerjään keskimääräinen paksuus?", "1,4km", "2,5km", "4,1km", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Kuinka nopeita Etelämantereen tuulet voivat olla pahimmillaan?", "35m/s", "235km/h", "320km/h", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionA("Montako millimetriä Etelämantereella sataa vuosittain?", "50mm", "89mm", "150mm", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionC("Kuinka monta prosenttia maapallon jäästä sijaitsee Etelämantereella?", "69 prosenttia", "79 prosenttia", "90 prosenttia", 20)
        kokonaispisteet_lista.append(result4)
        play_points = incident_risk2(1)
    elif planeNumber == 3:
        result1 = QuestionA("Montako millimetriä Etelämantereella sataa vuosittain?", "50mm", "89mm", "150mm", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Kuinka monta prosenttia maapallon jäästä sijaitsee Etelämantereella?", "69 prosenttia", "79 prosenttia", "90 prosenttia", 20)
        kokonaispisteet_lista.append(result2)
        play_points = incident_risk2(2)
    elif planeNumber == 4:
        result1 = QuestionB("Paljonko on Etelämantereen mannerjään keskimääräinen paksuus?", "1,4km", "2,5km", "4,1km", 20)
        kokonaispisteet_lista.append(result1)
        play_points = incident_risk2(3)
    return kokonaispisteet_lista, play_points


def travel_questionsAS(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = '{planeNumber}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")
    input("Paina Enter jatkaaksesi. ")

    kokonaispisteet_lista = []
    rip = False
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionC("Missä maassa sijaitsee maailman korkein vapaasti seisova lipputanko (165m)?", "Kiinassa", "Bhutanissa", "Tadzikistanissa", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Montako maatilaa on Singaporessa?", "9", "37", "0", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionA("Malediivit sijaitsee Intian valtamerellä ja on maailman matalin valtio. "
                            "Paljonko sen korkeus on keskimäärin merenpinnasta?", "2,1m", "3,2m", "5,5m", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionB("Montako jokea virtaa Saudi-Arabiassa?", "1", "0", "3", 20)
        kokonaispisteet_lista.append(result4)
        rip = incident_risk3(1)
    elif planeNumber == 3:
        result1 = QuestionC("Missä maassa sijaitsee maailman korkein vapaasti seisova lipputanko (165m)?", "Kiinassa", "Bhutanissa", "Tadzikistanissa", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionB("Montako jokea virtaa Saudi-Arabiassa?", "1", "0", "3", 20)
        kokonaispisteet_lista.append(result2)
        rip = incident_risk3(2)
    elif planeNumber == 4:
        result1 = QuestionC("Montako maatilaa on Singaporessa?", "9", "37", "0", 20)
        kokonaispisteet_lista.append(result1)
        rip = incident_risk3(3)
    return kokonaispisteet_lista, rip


def travel_questionsEU(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = '{planeNumber}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")
    input("Paina Enter jatkaaksesi. ")

    rip = False
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionC("Monelleko aikavyöhykkeelle Ranska ulottuu, kun otetaan huomioon sen territoriot ja alusmaat?", "5", "9", "12", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionA("Missä maassa sijaitsee Longyearbyen kaupunki, jossa 'kuoleminen on kiellettyä', "
                            "koska kylmyyden vuoksi ruumiit eivät maadu?", "Norjassa", "Ruotsissa", "Islannissa", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionA("Missä maassa sijaitsee mikrovaltio Ladonia?", "Ruotsissa", "Italiassa", "Kreikassa", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionB("Kuinka suuri osa Kosovon asukkaista on alle 25-vuotiaita?", "Neljännes", "Puolet", "Noin 10%", 20)
        kokonaispisteet_lista.append(result4)
        rip = incident_risk4(1)
    elif planeNumber == 3:
        result1 = QuestionB("Kuinka suuri osa Kosovon asukkaista on alle 25-vuotiaita?", "Neljännes", "Puolet", "Noin 10%", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionB("Missä maassa sijaitsee Longyearbyen kaupunki, jossa 'kuoleminen on kiellettyä', "
                            "koska kylmyyden vuoksi ruumiit eivät maadu?", "Ruotsissa", "Norjassa", "Islannissa", 20)
        kokonaispisteet_lista.append(result2)
        rip = incident_risk4(2)
    elif planeNumber == 4:
        result1 = QuestionA("Missä maassa sijaitsee Longyearbyen kaupunki, jossa 'kuoleminen on kiellettyä', "
                            "koska kylmyyden vuoksi ruumiit eivät maadu?", "Norjassa", "Ruotsissa", "Islannissa", 20)
        kokonaispisteet_lista.append(result1)
        rip = incident_risk4(3)
    return kokonaispisteet_lista, rip


def travel_questionsNA(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = '{planeNumber}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")
    input("Paina Enter jatkaaksesi. ")

    rip = False
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionB("Mitä Guamin saarelta ei löydy lainkaan?", "Asfalttia", "Hiekkaa", "Soraa", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Kuinka pitkä on Kanadan rantaviiva?", "130 421 kilometriä", "190 134 kilometriä", "202 080 kilometriä", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionB("Montako kansallispuistoa Yhdysvalloissa on?", "32", "58", "101", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionA("Montako ihmistä Meksikossa on kadonnut viimeisen vuosikymmenen aikana?", "Yli 27 000", "Noin 9000", "Noin 15 000", 20)
        kokonaispisteet_lista.append(result4)
        rip = incident_risk5(1)
    elif planeNumber == 3:
        result1 = QuestionA("Montako ihmistä Meksikossa on kadonnut viimeisen vuosikymmenen aikana?", "Yli 27 000", "Noin 9000", "Noin 15 000", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Kuinka pitkä on Kanadan rantaviiva?", "130 421 kilometriä", "190 134 kilometriä", "202 080 kilometriä", 20)
        kokonaispisteet_lista.append(result2)
        rip = incident_risk5(2)
    elif planeNumber == 4:
        result1 = QuestionB("Mitä Guamin saarelta ei löydy lainkaan?", "Asfalttia", "Soraa", "Hiekkaa", 20)
        kokonaispisteet_lista.append(result1)
        rip = incident_risk5(3)
    return kokonaispisteet_lista, rip


def travel_questionsOC(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = '{planeNumber}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")
    input("Paina Enter jatkaaksesi. ")

    rip = False
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionA("Minkä valtion virallisia kolikoita koristavat Pokemon-, Disney- ja Star Wars -hahmot?", "Niue", "Australia", "Uusi-Seelanti", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionB("Montako maata Oseaniaan kuuluu?", "12", "23", "18", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionB("Montako kengurulajia Australiassa on?", "27", "Yli 50", "Yli 90", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionC("Paljonko painoindeksi on Naurussa asukasta kohden?", "20-21", "26-28", "34-35", 20)
        kokonaispisteet_lista.append(result4)
        rip = incident_risk6(1)
    elif planeNumber == 3:
        result1 = QuestionB("Montako maata Oseaniaan kuuluu?", "12", "23", "18", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Minkä valtion virallisia kolikoita koristavat Pokemon-, Disney- ja Star Wars -hahmot?", "Uusi-Seelanti", "Australia", "Niue", 20)
        kokonaispisteet_lista.append(result2)
        rip = incident_risk6(2)
    elif planeNumber == 4:
        result1 = QuestionA("Minkä valtion virallisia kolikoita koristavat Pokemon-, Disney- ja Star Wars -hahmot?", "Niue", "Australia", "Uusi-Seelanti", 20)
        kokonaispisteet_lista.append(result1)
        rip = incident_risk6(3)
    return kokonaispisteet_lista, rip


def travel_questionsSA(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = '{planeNumber}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")
    input("Paina Enter jatkaaksesi. ")

    rip = False
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionA("Montako prosenttia Surinamen pinta-alasta on metsää?", "94,6 prosenttia", "73,1 prosenttia", "53,4 prosenttia", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Venezuelassa sijaitsee Heladeria Coromoto -jäätelöbaari, jossa on maailman "
                            "laajin makuvalikoima. Montako eri jäätelömakua siellä on saatavilla?", "91", "157", "860", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionB("Montako miljoonakaupunkia Brasiliassa on?", "7", "13", "21", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionA("Montako valtiota Etelä-Amerikassa on?", "12", "17", "9", 20)
        kokonaispisteet_lista.append(result4)
        rip = incident_risk7(1)
    elif planeNumber == 3:
        result1 = QuestionC("Venezuelassa sijaitsee Heladeria Coromoto -jäätelöbaari, jossa on maailman "
                            "laajin makuvalikoima. Montako eri jäätelömakua siellä on saatavilla?", "91", "157", "860", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionA("Montako valtiota Etelä-Amerikassa on?", "12", "17", "9", 20)
        kokonaispisteet_lista.append(result2)
        rip = incident_risk7(2)
    elif planeNumber == 4:
        result1 = QuestionB("Montako miljoonakaupunkia Brasiliassa on?", "7", "13", "21", 20)
        kokonaispisteet_lista.append(result1)
        rip = incident_risk7(3)
    return kokonaispisteet_lista, rip


def which_question(continent_abb, planeNro):
    kokonaispisteet_funktiossa = 0
    if continent_abb == AF:
        result = travel_questionsAF(planeNro)
        kokonaispisteet_lista = result[0]
        rip = result[1]
        return kokonaispisteet_lista, rip
    elif continent_abb == AN:
        result = travel_questionsAN(planeNro)
        kokonaispisteet_lista = result[0]
        morepoints = result[1]
        kokonaispisteet_funktiossa += morepoints
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == AS:
        result = travel_questionsAS(planeNro)
        kokonaispisteet_lista = result[0]
        lesspoints = result[1]
        kokonaispisteet_funktiossa -= lesspoints
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == EU:
        result = travel_questionsEU(planeNro)
        kokonaispisteet_lista = result[0]
        lesspoints = result[1]
        kokonaispisteet_funktiossa -= lesspoints
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == NA:
        result = travel_questionsNA(planeNro)
        kokonaispisteet_lista = result[0]
        morepoints = result[1]
        kokonaispisteet_funktiossa += morepoints
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == OC:
        result = travel_questionsOC(planeNro)
        kokonaispisteet_lista = result[0]
        lesspoints = result[1]
        kokonaispisteet_funktiossa -= lesspoints
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == SA:
        result = travel_questionsSA(planeNro)
        kokonaispisteet_lista = result[0]
        points_received = result[1]
        if result[1] == True:
            kokonaispisteet_funktiossa += points_received
        else:
            kokonaispisteet_funktiossa -= points_received
        return kokonaispisteet_lista, kokonaispisteet_funktiossa




# --- --- random eventit
def incident_risk1(luku):
    incident = random.randint(1,5)
    rip = False
    if incident <= luku:
        kolikko = random.choice(["Kruuna", "Klaava"])
        print("Lentokoneesi on syöksylaskussa!")
        print(f'Teitä on enää kaksi lentokoneessa, mutta tarjolla on vain yksi laskuvarjo.')
        print(f'Päätätte selvittää kolikonheitolla, kumpi teistä saa laskuvarjon.')
        print(f'Jos kolikko laskeutuu {kolikko} puoli ylöspäin, sinä saat sen.')
        print()
        input("Paina 'Enter' jatkaaksesi")

        kolikonheitto_satunnainen = "Kruuna" if random.randint(0, 1) > 0.5 else "Klaava"

        for aika in range(3, 0, -1):
            print(aika)
            time.sleep(1)

        print(kolikonheitto_satunnainen)

        if kolikko == kolikonheitto_satunnainen:
            print("Selvisit! Laskeudut turvallisesti seuraavalle lentokentälle.")
        else:
            print("Onni ei suosinut sinua! Joudut palaamaan edelliselle lentokentälle.")
            rip = True
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return rip



# PALAUTA POINTS EI RIP !!
def incident_risk2(luku):
    incident = random.randint(1,5)
    points = 0

    if incident <= luku:
        print("Löysit lottolipun maasta!")
        print("Syötä lappuun kaksi arpanumeroa yksi kerrallaan ja käy lunastamassa se läheiseltä kioskilta.")
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
            points = 10
        else:
            print(f'Valitettavasti arpaonni ei suosinut tällä kertaa, voittonumerot olisi olleet: {voittonumerot}')
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points


#tästä vähenee pisteet!!!
def incident_risk3(luku):
    incident = random.randint(1,5)
    points = 0
    if incident <= luku:
        vastaus_a = "Jatka kohti vessaa"
        vastaus_b = "Pahoittele ja anna 2 pistettä"

        print("Lähdet lentokoneessa vessaan, murra matkallasi tönäiset vahingossa ärtyisän oloista mieshenkilöä.")
        print("Mies kääntää päänsä ja vaikuttaa nyt hyvin vihaiselta.")
        print()
        print("Mitä teet?")
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
                    print("Mieshenkilö ei vaikutakaan enää kovin vihaiselta ja haluaa tarjota sinulle huikan. Mitä teet?")
                    print()
                    print("A: Jatka matkaasi vessaan")
                    print("B: Ota huikka miehen vihreästä pullosta")
                    vaihtoehdot = ["a", "b"]
                    print()
                    valinta = input("Vastauksesi: ").lower()
                    if valinta == "a":
                        print("'Wrong answer pal...'")
                        print()
                        print("Heräät lentokoneen ensiapuvuoteelta, hoitokulusi ovat 4 pistettä.")
                        points = 4
                    toiminta = False

                    if valinta == "b":
                        print("          Otat huikan...")
                        print("...askel vaikuttaa heti keveämmältä...")
                        print()
                        print("Voit jatkaa matkaasi.")
                    toiminta = False

                elif pelaaja == "b":
                    print("'You got lucky this time, pal...'")
                    print()
                    print("Selvisit säikähdyksellä, onneksi ei käynyt pahemmin...")
                toiminta = False
    else:
        print("Saavuit kohteeseen turvallisesti!")
    return points


# pisteet vähenee
def incident_risk4(luku):
    incident = random.randint(1,5)
    points = 0
    if incident <= luku:
        print("Törmäät lentokentän käytävällä kodittomaan henkilöön.")
        print("Hän anelee sinulta yhtä pistettä.")
        print()
        valinta = input("Annatko pisteen? (kyllä/ei) ")

        if valinta.lower() == "kyllä" or "k":
            print("Annoit pisteen.")
            points = 1
        if valinta.lower() == "ei" or "e":
            print("Koditon: :-(")
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points


# lisää pisteitä
def incident_risk5(luku):
    incident = random.randint(1,5)
    points = 0

    if incident <= luku:
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
            print(f'Onnea, voitit 5 pistettä! Aikaa kului {round(time_elapsed, 2)} sekuntia.')
            points = 5
        else:
            print(f'Hävisit:(. Kokonaistuloksesi oli {pisteet}/100.')
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points


# pisteet vähenee
def incident_risk6(luku):
    incident = random.randint(1,5)
    points = 0
    if incident <= luku:
        vastaus_a = "Osta oma lippu (-2 pistettä)"
        vastaus_b = "Yritä anastaa lippu"

        print("On aika hankkia lentoliput seuraavaan kohteeseen.")
        print("Olet matkalla kohti lippupistettä, kun huomaat penkillä nukkuvan vanhuksen, jonka taskusta pilkistää lentolippu.")
        print()
        print("Voit yrittää anastaa lipun häneltä tai hakea oman viidellä pisteellä.")
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
                    print("B: Käänny ja osta oma lippusi (-2 pistettä)")
                    vaihtoehdot = ["a", "b"]
                    print()
                    valinta = input("Vastauksesi: ").lower()
                    if valinta == "b":
                        print("Ostit oman lipun ':D'")
                        points = 2
                    toiminta = False

                    if valinta == "a":
                        print("Sait lipun... Pakenet...")
                        print()
                        print("Matkallasi kohti lähtöselvitystä vartija pysäyttää sinut.")
                        print("Turvakameratalleenteesta on selvinnyt, että varastit lipun.")
                        print()
                        print("Rangaistukseksi saat 4 pisteen sakon.")
                        points = 4

                    toiminta = False

                elif pelaaja == "a":
                    print("Ostit oman lipun ':D'")
                    points = 2
                toiminta = False
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points



# SOS molempiin mahdollisuus
def incident_risk7(luku):
    incident = random.randint(1,5)
    points = 0
    add_points = True
    if incident <= luku:
        print("Sinut haastetaan 'kivi, paperi, sakset' -peliin.")
        print("Voit joko voittaa tai hävitä yhden pisteen.")
        print()
        print("Syötä valintasi, kun olet valmis aloittamaan.")

        vaihtoehdot = ("kivi", "paperi", "sakset", "liimapuikko")
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

            print(f'Sinä: {pelaaja}')
            print(f'Vastustaja: {tietokone}')

            if pelaaja == tietokone:
                print("Tasapeli! Uusintakierros.")
                print()

            elif pelaaja == "kivi" and tietokone == "sakset":
                print("Sinä voitit! (+1 piste)")
                points = 1

            elif pelaaja == "paperi" and tietokone == "kivi":
                print("Sinä voitit! (+1 piste)")
                points = 1

            elif pelaaja == "sakset" and tietokone == "paperi":
                print("Sinä voitit! (+1 piste)")
                points = 1

            if pelaaja == "liimapuikko":
                print("Saat viisi pistettä luovuudesta :D")
                points = 5

            else:
                print("Sinä hävisit. (-1 piste)")
            toiminta = False
            add_points = False
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points, add_points







# --- --- pääohjelma --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# alkumäärittelyjä
kokonaispisteet_lista = []
kokonaispisteet_summa = 0
aikaakulunut = 0
MainGameOver = False

AF = False
AN = False
AS = False
EU = False
NA = False
OC = False
SA = False


# asking username and welcoming player
welcome()
user = get_user()
timenoprint(1)


# --- MAIN PELI:

while MainGameOver == False:
    # lentokoneen ja lähtöpaikan valinta
    result = choose_plane()
    planeNumber = result[0]
    plane = result[1]

    result = choose_start()
    start_airport = result[0]
    start_continent = result[1]


    # ensimmäisen matkakohteen valinta
    print()
    result = travel()
    travel_airport = result[0]
    travel_ident = result[1]
    travel_continent = result[2]
    MainGameOver = result[3]


    peliohjeet()

    # 1. kohde
    result = which_question(travel_continent, travel_airport)
    kokonaispisteet_lista = result[0]
    pisteitä = result[1]

    result = pistelaskuri(kokonaispisteet_lista)
    kokonaispisteet_summa = result[0] + (pisteitä)
    print(f"Sinulla on tällä hetkellä {kokonaispisteet_summa} pistettä")
    aikaakulunut = result[1]


    # 2. kohde
    print()
    result = travel()
    travel_airport = result[0]
    travel_ident = result[1]
    travel_continent = result[2]
    MainGameOver = result[3]


    result = which_question(travel_continent, travel_airport)
    kokonaispisteet_lista = result[0]
    pisteitä = result[1]

    result = pistelaskuri(kokonaispisteet_lista)
    kokonaispisteet_summa = result[0] + (pisteitä)
    print(f"Sinulla on tällä hetkellä {kokonaispisteet_summa} pistettä")
    aikaakulunut = result[1]


    # 3. kohde
    print()
    result = travel()
    travel_airport = result[0]
    travel_ident = result[1]
    travel_continent = result[2]
    MainGameOver = result[3]


    result = which_question(travel_continent, travel_airport)
    kokonaispisteet_lista = result[0]
    pisteitä = result[1]

    result = pistelaskuri(kokonaispisteet_lista)
    kokonaispisteet_summa = result[0] + (pisteitä)
    print(f"Sinulla on tällä hetkellä {kokonaispisteet_summa} pistettä")
    aikaakulunut = result[1]



    # 4. kohde
    print()
    result = travel()
    travel_airport = result[0]
    travel_ident = result[1]
    travel_continent = result[2]
    MainGameOver = result[3]


    result = which_question(travel_continent, travel_airport)
    kokonaispisteet_lista = result[0]
    pisteitä = result[1]

    result = pistelaskuri(kokonaispisteet_lista)
    kokonaispisteet_summa = result[0] + (pisteitä)
    print(f"Sinulla on tällä hetkellä {kokonaispisteet_summa} pistettä")
    aikaakulunut = result[1]




    # 5. kohde
    print()
    result = travel()
    travel_airport = result[0]
    travel_ident = result[1]
    travel_continent = result[2]
    MainGameOver = result[3]


    result = which_question(travel_continent, travel_airport)
    kokonaispisteet_lista = result[0]
    pisteitä = result[1]

    result = pistelaskuri(kokonaispisteet_lista)
    kokonaispisteet_summa = result[0] + (pisteitä)
    print(f"Sinulla on tällä hetkellä {kokonaispisteet_summa} pistettä")
    aikaakulunut = result[1]




    # 6. kohde
    print()
    result = travel()
    travel_airport = result[0]
    travel_ident = result[1]
    travel_continent = result[2]
    MainGameOver = result[3]


    result = which_question(travel_continent, travel_airport)
    kokonaispisteet_lista = result[0]
    pisteitä = result[1]

    result = pistelaskuri(kokonaispisteet_lista)
    kokonaispisteet_summa = result[0] + (pisteitä)
    print(f"Sinulla on tällä hetkellä {kokonaispisteet_summa} pistettä")
    aikaakulunut = result[1]



    # 7. kohde
    print()
    result = travel()
    travel_airport = result[0]
    travel_ident = result[1]
    travel_continent = result[2]
    MainGameOver = result[3]


    result = which_question(travel_continent, travel_airport)
    kokonaispisteet_lista = result[0]
    pisteitä = result[1]

    result = pistelaskuri(kokonaispisteet_lista)
    kokonaispisteet_summa = result[0] + (pisteitä)
    print(f"Sinulla on tällä hetkellä {kokonaispisteet_summa} pistettä")
    aikaakulunut = result[1]




    choose_options()
    save_result(user, aikaakulunut, kokonaispisteet_summa, airport)

    choose_options()


    # game over screen
    # end()

print("Peli loppui.")