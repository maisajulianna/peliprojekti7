import pygame
import sys
import time


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
while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                sys.exit()

        logo_rect = logo_rect.move([1,-1])
        screen.fill(white)

        screen.blit(tarina, tarina_rect)
        screen.blit(logo, logo_rect)
        pygame.display.flip()
        time.sleep(0.01)
