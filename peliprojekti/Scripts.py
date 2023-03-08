import pygame
import sys
import time
import mysql.connector


# Tämä funktio näyttää tekstiä peliikkunassa.
def print_text(screen, message, x, y, font_color=(0,0,0),\
               font_type="C:/Users/natak/LentoPeli/images/magneto_bold.ttf",\
               font_size=20):
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
def get_user( ):

    yhteys = mysql.connector.connect(
        host='127.0.0.1',  # localhost
        port=3306,  # MariaDB port
        database='flight_game',
        user='userN',
        password='1234',
        autocommit=True)

    pygame.init()
    size = width, height = 600, 600
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("MVMN-Lentopeli")
    screen.fill(white)
    pygame.display.flip()
    print_text(screen, "Aloitetaan...", 10, 1)
    print_text(screen, "Anna sinun nimisi pelissamme...", 10, 30)
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
                        print_text(screen, "Anna sinun nimisi pelissamme...", 10, 30)
                        pygame.display.flip()
                        print_text(screen, user_name, 100, 30)

                    elif len(user_name) < 20:
                        user_name = user_name + event.unicode
                        print_text(screen, user_name, 100, 30)

    print_text(screen, "Hei, " + user_name + "!", 10, 90)
    time.sleep(3)
    #check if user_name already exists in the table game (not finished games)

    sql = "select * from game where screen_name = '" + user_name + "';"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchone()
    print (result)
    if not result:  #Jos tietokannassa ei ole samannimistä käyttäjää
        print_text (screen, user_name + ", sinulla ei ole keskeneräisiä pelejä.", 10, 120)
        print_text(screen, "Aloitetaan uusi peli hetken kuluttua...", 10, 150)
        # add user to DB
        sql = "insert into game values (NULL, 0,'" + user_name + "',"\
              " 0, NULL, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)"
        print (sql)
        kursori.execute(sql)
        sql = "select * from game where screen_name = '" + user_name + "';"
        kursori.execute(sql)
        user = kursori.fetchone()    # user - kaikki tiedot nykyisestä pelaajasta
        print (user)
        need_input = False
        time.sleep(3)
        pygame.quit()

    else: #Jos tietokannassa on samannimistä käyttäjää
        print_text(screen, "Olet jo aloittanut pelaamisen, jatkatko?", 10, 120)
        print_text(screen, "a - jatka viimeistä peliä", 10, 150)
        print_text(screen, "b - aloita uusi peli poistamalla vanhan pelin tulokset", 10, 180)
        print_text(screen, "c - vaihda pelaajan nimi", 10, 210)
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
                       yhteys.close()
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
                        yhteys.close()
                        need_input = False
                        time.sleep(3)
                    if event.key == pygame.K_c:
                        print_text(screen, "c", 10, 240)
                        need_input = False
                        yhteys.close()
                        pygame.quit()
                        user = get_user()  # Varoitus, rekursio!

    return user

# use it for saving results after each flight,
# this function return True if all continents are visited by user and
# False otherwise
def save_result(user, time_sec, score, airport):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',  # localhost
        port=3306,  # MariaDB port
        database='flight_game',
        user='userN',
        password='1234',
        autocommit=True)
    kursori = yhteys.cursor()

    # check where airport located
    sql = "select country.continent from country inner join airport" \
          " on country.iso_country=airport.iso_country where airport.ident ='"+airport+"';"
    kursori.execute(sql)
    continent = kursori.fetchone()

    """update player's results
    user[0] - id
    user[1] - time in sec
    user[2] - screen name
    user[3] - score
    user[4] - last_location
    user[5] - AF (afrikka)
    user[6] - AN (antarktikka)
    user[7] - AS (australia)
    user[8] - EU (europa)
    user[9] - NA (north amerika)
    user[10] - OC (australia and ocean) ??? 
    user[11] - SA (south america)
    """
    sql = "update game set last_location='" + str(airport) +"', time_sec=" + str(user[1] + time_sec) + "," \
                           " score=" + str(user[3]+score) + "," \
                           " " + continent[0] +"_=TRUE where player_id=" + str(user[0]) + ";"

    print (sql)
    kursori.execute(sql)


    # check if all continents were visited
    sql = "select  AF_*AN_*AS_*EU_*NA_*OC_*SA_ from game where player_id=" + str(user[0]) + ";"
    kursori.execute(sql)
    result = kursori.fetchone()
    result = bool(result[0])

    #if result = True all continents were visited, so we need to save result to table result
    if result:
        sql = "select * from game where player_id=" + str(user[0]) + ";"
        kursori.execute(sql)
        user = kursori.fetchone()
        """
        user[0] - id
        user[1] - time in sec
        user[2] - screen name
        user[3] - score
        """
        sql = "insert into results (player_id, screen_name, score, time_sec) " \
              "values ("+str(user[0])+", '" + str(user[2]) + "', " + str(user[3]) + ", " + str(user[1])+ ");"
        kursori.execute(sql)
    yhteys.close()

    return result

# use it if user would like to delete current game
def delete_game(user):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',  # localhost
        port=3306,  # MariaDB port
        database='flight_game',
        user='userN',
        password='1234',
        autocommit=True)
    kursori = yhteys.cursor()

    # delete current game of this user
    sql = "delete from game where player_id=" + str(user[0])+ ";"
    kursori.execute(sql)
    yhteys.close()

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
    yhteys = mysql.connector.connect(
        host='127.0.0.1',  # localhost
        port=3306,  # MariaDB port
        database='flight_game',
        user='userN',
        password='1234',
        autocommit=True)
    kursori = yhteys.cursor()
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
    pygame.quit()

#
# MAIN PROGRAMM
#
welcome()
user = get_user() # user on lista, jossa on kaikki tiedot pelaajasta

time_sec = 11
score = 100
airport = "AE-0004"

# use it for saving results after each flight,
# this function return True if all continents are visited by user and
# False otherwise
save_result(user, time_sec, score, airport)

# use it if user would like to delete current game
#delete_game(user)

#game over screen
end()







