import pygame
from plane_sprites import *

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./14_game/images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./14_game/images/me1.png")
screen.blit(hero, (150, 500))

pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)

enemy = GameSprite("./14_game/image/enemy1.png")
enemy1 = GameSprite("./14_game/images/enemy1.png", 2)
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()
    hero_rect.y -= 1
    if hero_rect.y <= 0:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()

pygame.quit()
