import pygame
import sys
import time
import mysql.connector


# Tämä funktio näyttää tekstiä peliikkunassa.
def print_text(message, x, y, font_color=(0,0,0),\
               font_type="C:/Users/natak/LentoPeli/images/magneto_bold.ttf", font_size=30):

    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x,y))
    pygame.display.flip()


#show welcome window

pygame.init()
size = width, height = 600, 600
speed = [1, 1]                  # lennon kuvan muutos videon aikana
black = 0, 0, 0
white = 255, 255, 255
position = 0                    # nykyinen lähtökohta
interspace = 50                 # riviväli

need_input = False

screen = pygame.display.set_mode(size)
logo = pygame.image.load("images/logo_game.png")
tarina = pygame.image.load("images/tarina.png")
logo_rect = logo.get_rect()
tarina_rect = tarina.get_rect()

logo_rect = logo_rect.move([1,height])
pygame.display.set_caption("MVMN-Lentopeli")
show_welcome = True

# Näytämme pelin tarinan ja lentävän lentokoneen, kunnes käyttäjä napsauttaa ENTER

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


#ask user_name

screen.fill(white)
pygame.display.flip()

print_text("Aloitetaan...", 1, position)
position +=
print_text("Anna sinun nimisi pelissamme (20 symbolia maksimumi)...", 1, 50)
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
                    print_text("Aloitetaan...", 0, 0)
                    print_text("Anna sinun nimisi pelissamme...", 1, 30)
                    pygame.display.flip()
                    print_text(user_name, 10, 60)

                elif len(user_name) < 20:
                    user_name = user_name + event.unicode
                    print_text(user_name, 10, 60)

print_text("Hei, " + user_name, 10, 90)
time.sleep(4)

yhteys = mysql.connector.connect(
         host='127.0.0.1',  #localhost
         port=3306,         #MariaDB port
         database='flight_game',
         user='userN',
         password='1234',
         autocommit=True)

#check if user_name already exists

sql = "select * from players where screen_name = '" + user_name + "';"

kursori = yhteys.cursor()

kursori.execute(sql)
result = kursori.fetchone()
print (result)
if not result:
    print ("no user" + user_name)
    # add user to DB

    sql = "insert into players values (NULL, NULL,'" + user_name + "', NULL, NULL, NULL,NULL,NULL,NULL,NULL,NULL,NULL)"
    kursori.execute(sql)
else:
    print_text("Olet jo aloittanut pelaamisen, jatkatko?", 10, 500, font_size = 20)
    print_text("A - jatka viimeistä peliä", 10, 520, font_size = 20)
    print_text("B - aloita uusi peli poistamalla vanhan pelin tulokset", 10, 530, font_size = 20)
    need_input = True
    while need_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if need_input and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                   user = result            # user - kaikki tiedot nykyisestä pelaajasta
                if event.key == pygame.K_b:    # "vanha" pelaaja aloittaa uuden pelin -
                                               # on poistettava kaikki tiedot edellisestä pelistä
                    sql = "update players set AF_= NULL, AN_ = NULL, AS_ = NULL, " + \
                          "EU_= NULL,NA_ = NULL, OC_= NULL,SA_ = NULL, time_sec = NULL, " + \
                          "score = NULL where player_id=" + str(result[0])
                    kursori.execute(sql)
                    sql = "select * from players where player_id=" + str(result[0])
                    kursori.execute(sql)
                    user = kursori.fetchone()

                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[0:-1]
                    screen.fill(white)
                    print_text("Aloitetaan...", 0, 0)
                    print_text("Anna sinun nimisi pelissamme...", 4, 30)
                    pygame.display.flip()
                    print_text(user_name, 10, 300)

                elif len(user_name) < 20:
                    user_name = user_name + event.unicode
                    print_text(user_name, 10, 300)

    print_text("Hei, " + user_name, 10, 400)
    time.sleep(5)



yhteys.close()

# save user_name in DB




"""

sql_save_user_name =   "insert into players values (0,'" + user_name + "');"
print (sql_save_user_name)
kursori = yhteys.cursor()

kursori.execute(sql_save_user_name)

yhteys.close()

print("kaikki on ok")
"""



