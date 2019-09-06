import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./14_game/images/background.png")
screen.blit(bg, (0, 0))
pygame.display.update()

hero = pygame.image.load("./14_game/images/me1.png")
screen.blit(hero, (150, 500))
pygame.display.update()

while True:
    pass

pygame.quit()
