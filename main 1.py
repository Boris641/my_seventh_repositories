import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/shutery.jpg")
pygame.display.set_icon(icon)

target_ing = pygame.image.load("img/target.png")
target_width = 80
target_heigth = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGTH - target_heigth)

color = (random.randint(a=0, b=255), random.randint(a=0, b=255), random.randint(a=0, b=255))

score = 0
score_font = pygame.font.Font(None,36)


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_heigth:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGTH - target_heigth)
                score += 1
    screen.blit(target_ing, (target_x, target_y))

    score_text = score_font.render("Количество очков : "+str(score), True,(255,255,255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()


