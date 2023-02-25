import pygame
import sys
import time

def print_text(message, x, y, font_color=(0,0,0), font_type="C:/Users/natak/LentoPeli/images/magneto_bold.ttf", font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x,y))


def start_game():
    screen.fill(white)
    pygame.display.flip()
    time.sleep(2)
    print_text("Aloitetaan...", 0,0)
    pygame.display.flip()
    print_text("Anna sinun nimisi pelissamme...", 4, 30)
    pygame.display.flip()
    time.sleep(7)


pygame.init()

size = width, height = 600, 600
speed = [1, 1]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

logo = pygame.image.load("images\logo_game.png")
tarina = pygame.image.load("images/tarina.png")
logo_rect = logo.get_rect()
tarina_rect = tarina.get_rect()

logo_rect = logo_rect.move([1,480])
pygame.display.set_caption("MVMN-Lentopeli", "images\logo_game.png")
while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                sys.exit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                        start_game()

        logo_rect = logo_rect.move([1,-1])

        screen.fill(white)
        screen.blit(tarina, tarina_rect)
        screen.blit(logo, logo_rect)
        pygame.display.flip()
        time.sleep(0.01)


