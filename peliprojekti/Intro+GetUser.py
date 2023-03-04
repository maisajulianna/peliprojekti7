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
                        print_text(screen, user_name, 10, 60)

                    elif len(user_name) < 20:
                        user_name = user_name + event.unicode
                        print_text(screen, user_name, 10, 60)

    print_text(screen, "Hei, " + user_name + "!", 10, 90)
    time.sleep(3)
    #check if user_name already exists in the table game (not finished games)

    sql = "select * from game where screen_name = '" + user_name + "';"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchone()

    if not result:  #Jos tietokannassa ei ole samannimistä käyttäjää
        print_text (screen, user_name + ", sinulla ei ole keskeneräisiä pelejä.", 10, 120)
        print_text(screen, "Aloitetaan uusi peli hetken kuluttua...", 10, 150)
        # add user to DB
        sql = "insert into game values (NULL, NULL,'" + user_name + "',"\
              " NULL, NULL, NULL,NULL,NULL,NULL,NULL,NULL,NULL)"
        kursori.execute(sql)
        sql = "select * from game where screen_name = '" + user_name + "';"
        kursori.execute(sql)
        user = kursori.fetchone()    # user - kaikki tiedot nykyisestä pelaajasta
        need_input = False

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
                        sql = "update game set AF_= NULL, AN_ = NULL, AS_ = NULL, " + \
                              "EU_= NULL,NA_ = NULL, OC_= NULL,SA_ = NULL, time_sec = NULL, " + \
                              "score = NULL where player_id=" + str(result[0])
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


# main programm
welcome()
user = get_user() # kaikki tiedot pelaajasta

time = 11
pisteet = 100
airport = "AE-0004"
# use it for saving results after each flight,
# this function return True if all continents are visited by user and False otherwise
save_result(user, time, score, airport)

delete_game(user) # use it if user would like to delete current game


print ("game over ")
print (user)




"""

sql_save_user_name =   "insert into players values (0,'" + user_name + "');"
print (sql_save_user_name)
kursori = yhteys.cursor()

kursori.execute(sql_save_user_name)

yhteys.close()

print("kaikki on ok")
"""



