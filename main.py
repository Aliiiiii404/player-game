from os import X_OK
import pygame
from pygame import draw
import random
from pygame import mixer
import time
from PIL import Image

pygame.init()
mixer.init()
#constant
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREY = (169,169,169)
SPEED = 10
TEXT_FONT = pygame.font.SysFont('comicsans', 20)
FPS = 144

clock = pygame.time.Clock()
score = 0
level = 0
player_helth = 200
level_goals = [5, 10, 15, 20, 25]
#rendom rects
random_top = random.randint(0, 400)
random_left = random.randint(0, 200)
random_width = random.randint(0, 80)
random_height = random.randint(0, 80)
#player image
player = pygame.image.load("./Assets/player.png").convert_alpha()
player = pygame.transform.scale(player, (60, 60)) 
rect = player.get_rect(x=0, y=0)
#food image
food = pygame.image.load("./Assets/food.png").convert_alpha()
food = pygame.transform.scale(food, (60, 60)) 
#background sound
mixer.music.load("./Assets/background.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.1)

obstacle = pygame.Rect(random_left, random_top, random_width, random_height)

def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

def drawScore():
    global score, level_goals, level
    if score == level_goals[level]:
        level += 1
    text = TEXT_FONT.render("Diamond Amount : " + str(score) + "/" + str(level_goals[level]) , 1, BLACK)
    text_rect = text.get_rect(center=(WIDTH - 100, HEIGHT - 20))
    SCREEN.blit(text, text_rect)

def drawLevel():
    global level
    text = TEXT_FONT.render("LEVEL : " + str(level), 1, BLACK)
    text_rect = text.get_rect(center=(WIDTH - 50, 20))
    SCREEN.blit(text, text_rect)

def drawFood():
    global food, obstacle
    SCREEN.blit(food, obstacle)

def darwHelthBar():
    pygame.draw.rect(SCREEN, RED, (50, HEIGHT - 30, player_helth, 20))

def main():
    global run, rect, obstacle, player_helth, score, player, random_top, random_left, random_width, random_height
    run = True
    while run:
        clock.tick(FPS)
        quit_game()
        SCREEN.fill(WHITE)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and rect.x > 0:  # a gauche
            rect.x -= SPEED
        if keys_pressed[pygame.K_RIGHT] and rect.x < WIDTH-40:  # a droite
            rect.x += SPEED
        if keys_pressed[pygame.K_UP] and rect.y > 0:  # en haut
            rect.y -=SPEED
        if keys_pressed[pygame.K_DOWN] and rect.y < WIDTH-40:  # en bas
            rect.y +=SPEED

        if rect.colliderect(obstacle):
            random_top = random.randint(0, 400)
            random_left = random.randint(0, 200)
            random_width = random.randint(0, 80)
            random_height = random.randint(0, 80)
            score = score + 1
            obstacle = pygame.Rect(random_left, random_top, random_width, random_height)
            player_helth = player_helth + 10
        elif player_helth <= 0:
            run = False
            print("GAME OVER")
        else:
            player_helth = player_helth - 0.1


        player = pygame.transform.rotate(player, 0)
        SCREEN.blit(player, rect)
        drawFood()
        darwHelthBar()
        drawScore()
        drawLevel()
        pygame.time.delay(30)
        pygame.display.update()

if __name__ == "__main__":
    main()



    
