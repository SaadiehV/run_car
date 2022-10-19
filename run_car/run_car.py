import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.font.init()

def load_asset(asset_name):
    return pygame.image.load(asset_name).convert_alpha()

def scale_asset(asset_name, x, y):
    return pygame.transform.scale(asset_name, (x, y))

def rotate_asset(asset_name, angle):
    return pygame.transform.rotate(asset_name, angle)

height = 900
#Laddar in alla assets, skapar äver roterade versioner av vissa assets för att få "svängbilder"
screen = pygame.display.set_mode((800,height))
bg_img = load_asset("assets/bg_image.png")
bg = scale_asset(bg_img, 800, height)

car_straight = load_asset("assets/car_straight.pcx")
car_straight = scale_asset(car_straight, 55, 110)
car_left = rotate_asset(car_straight, 30)
car_right = rotate_asset(car_straight, -30)

broken_straight = load_asset("assets/broken_straight.pcx")
broken_left = rotate_asset(broken_straight, 30)
broken_right = rotate_asset(broken_straight, -30)

logo = load_asset("assets/logo.png")

start_game = load_asset("assets/start_game.png")
start_game_hover = load_asset("assets/start_game_hover.png")

quit_logo = load_asset("assets/quit.png")
quit_hover = load_asset("assets/quit_hover.png")

score_pic = load_asset("assets/score.png")
score_pic = scale_asset(score_pic, 130, 40)

#Hämtar koordinat av bilders mittpunkt för att enklare centrera.
logo_center = logo.get_rect(center=(400,150))
start_game_center = start_game.get_rect(center=(400,400))
quit_center = quit_logo.get_rect(center=(400,550))

y = 0
x = 350
y_car = 750
car = car_straight
score = 0
speed = 1
quit_button = quit_logo
start = start_game
start_screen = True
running = False
font = pygame.font.Font("assets/font.ttf", 30)

def draw_bg():
    global y
    if y >= height:
        y = 0
    screen.fill((0,0,0))
    screen.blit(bg, (0 , y))
    screen.blit(bg, (0 , -height+y))

def draw_ss():
    global y
    screen.blit(logo, logo_center)
    screen.blit(start, start_game_center)
    screen.blit(quit_button, quit_center)
    screen.blit(car_straight, (x,750))
    y += speed
    pygame.display.flip()

def draw_game():
    global y
    global score
    screen.blit(car, (x,y_car))
    screen.blit(score_pic, (0, 860))
    y += speed
    score_text = font.render(str(int(score)), True, (255,255,255))
    score += 0.1
    screen.blit(score_text, (140, 860))

def ss_buttons():
    global start
    global quit_button
    global start_screen
    global running
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

def controls():
    global car
    global x
    global y_car
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

while start_screen:
    draw_bg()
    draw_ss()   
    ss_buttons()

while running:
    draw_bg()
    draw_game()
    controls()
    
