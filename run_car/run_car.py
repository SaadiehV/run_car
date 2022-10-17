import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.font.init()
height = 900
screen = pygame.display.set_mode((800,height))
bg_img = pygame.image.load("assets/bg_image.png").convert_alpha()
bg = pygame.transform.scale(bg_img, (800,height))
y = 0
x = 350
y_car = 750


#Laddar in alla assets, skapar äver roterade versioner av vissa assets för att få "svängbilder"
car_straight = pygame.image.load("assets/car_straight.pcx").convert_alpha()
car_straight = pygame.transform.scale(car_straight, (55, 110))
car_left = pygame.transform.rotate(car_straight, 30)
car_right = pygame.transform.rotate(car_straight, -30)
broken_straight = pygame.image.load("assets/broken_straight.pcx").convert_alpha()
broken_left = pygame.transform.rotate(broken_straight, 30)
broken_right = pygame.transform.rotate(broken_straight, -30)
logo = pygame.image.load("assets/logo.png").convert_alpha()
start_game = pygame.image.load("assets/start_game.png").convert_alpha()
start_game_hover = pygame.image.load("assets/start_game_hover.png").convert_alpha()
quit_logo = pygame.image.load("assets/quit.png").convert_alpha()
quit_hover = pygame.image.load("assets/quit_hover.png").convert_alpha()
score_pic = pygame.image.load("assets/score.png").convert_alpha()
score_pic = pygame.transform.scale(score_pic, (130, 40))

#Hämtar koordina av bilder för att enklare centrera.

logo_center = logo.get_rect(center=(400,150))
start_game_center = start_game.get_rect(center=(400,400))
quit_center = quit_logo.get_rect(center=(400,550))


score = 0
speed = 1
quit_button = quit_logo
start = start_game
start_screen = True
running = False
spunk = pygame.font.Font("assets/font.ttf", 30)
while start_screen:  
    if y >= height:
        y = 0
    screen.fill((0,0,0))
    screen.blit(bg, (0 , y))
    screen.blit(bg, (0 , -height+y))
    screen.blit(logo, logo_center)
    screen.blit(start, start_game_center)
    screen.blit(quit_button, quit_center)
    screen.blit(car_straight, (x,750))
    y += speed
    pygame.display.flip()


    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(start_game_center, mouse):
            start = start_game_hover
        else:
            start = start_game

        if pygame.Rect.collidepoint(quit_center, mouse):
            quit_button = quit_hover
        else:
            quit_button = quit_logo
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if pygame.Rect.collidepoint(start_game_center, mouse):
                start_screen = False
                running = True
            elif pygame.Rect.collidepoint(quit_center, mouse):
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)
                running = False

car = car_straight
while running:
    if y >= height:
        y = 0
    screen.fill((0,0,0))
    screen.blit(bg, (0 , y))
    screen.blit(bg, (0 , -height+y))
    screen.blit(car, (x,y_car))
    screen.blit(score_pic, (0, 860))
    y += speed
    score_text = spunk.render(str(int(score)), True, (255,255,255))
    score += 0.1
    screen.blit(score_text, (140, 860))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and x < 666:
        car = car_right
        x += 1
    elif keys[pygame.K_a] and x > 80:
        car = car_left
        x -= 1
    else:
        car = car_straight

    if keys[pygame.K_w] and y_car > 200:
        y_car -= 0.5
    elif keys[pygame.K_w] == False and y_car < 750:
        y_car += 0.5
   
    for event in pygame.event.get():      
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit(0)
                    running = False

    pygame.display.flip()
