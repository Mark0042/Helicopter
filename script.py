import pygame
import math
import random
from pygame import mixer

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
mixer.music.load("whirring.mp3")
mixer.music.play(-1)

background=pygame.image.load("background.jpeg")



pygame.display.set_caption("Helicopter")

playerImage = pygame.image.load("travel.png")
playerX = 100
playerY = 300
playerX_change = 0
playerY_change = 0
pipeImage = pygame.image.load("pipe.png")
pipeX = 400
pipeY = random.randint(300,500)
pipeX_change = 0
pipeImage2 = pygame.image.load("pipe2.png")
pipe2X = pipeX+random.randint(80,400)
pipe2Y = random.randint(-200,-10)
pipe2X_change = 0
pipeImage3 = pygame.image.load("pipe.png")
pipe3X = pipe2X+random.randint(70,400)
pipe3Y = random.randint(300,500)
pipe3X_change = 0
pipeImage4 = pygame.image.load("pipe2.png")
pipe4X = pipe3X+random.randint(90,400)
pipe4Y = random.randint(-200,-10)
pipe4X_change = 0



def player(x, y):
    screen.blit(playerImage, (x, y))

def pipe(x, y):
    screen.blit(pipeImage, (x, y))
def pipe2(x, y):
    screen.blit(pipeImage2, (x, y))
def pipe3(x, y):
    screen.blit(pipeImage, (x, y))
def pipe4(x, y):
    screen.blit(pipeImage2, (x, y))
def iscolliding1(x1,y1,x2,y2):
    if abs(x1-x2)<=50 and (y2-y1)<50:
        return True
    return False
def iscolliding2(x1,y1,x2,y2):
    if abs(x1-x2)<=55 and (y1-y2)<315:
        return True
    return False
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x,y))

over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200,250))




running = True
cnt=0
fct=1
flag1=1
flag2=1
flag3=1
flag4=1
gameover=False
while running:
    cnt+=1
    screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerY_change=-(4*fct)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playerY_change=(3*fct)
        if cnt>=1000 and fct<=5:
            cnt=1000
            fct+=0.05
    playerY+=playerY_change

    pipeX-=(5*fct)
    if pipeX<=-60:
        pipeX = 800
        pipeY = random.randint(300, 500)
        flag1=1
    pipe2X -= (5*fct)
    if pipe2X <= -60:
        pipe2X = 800
        pipe2Y = random.randint(-200,-10)
        flag2=1
    pipe3X-=(5*fct)
    if pipe3X<=-60:
        pipe3X = 800
        pipe3Y = random.randint(300, 500)
        flag3=1
    pipe4X -= (5*fct)
    if pipe4X <= -60:
        pipe4X = 800
        pipe4Y = random.randint(-200,-10)
        flag4=1
    collided=False

    bool1=iscolliding1(playerX,playerY,pipeX,pipeY)
    bool2=iscolliding2(playerX,playerY,pipe2X,pipe2Y)
    bool3=iscolliding1(playerX,playerY,pipe3X,pipe3Y)
    bool4=iscolliding2(playerX,playerY,pipe4X,pipe4Y)


    if playerY>=526 or playerY<=0 or bool1 or bool2 or bool3 or bool4:
        game_over_text()
        playerX = 5000
        playerY = 5000
        gameover=True
    if playerX>=pipeX and flag1 and not gameover:
        score_value+=10
        flag1=0
    if playerX>=pipe2X and flag2 and not gameover:
        score_value+=10
        flag2=0
    if playerX>=pipe3X and flag3 and not gameover:
        score_value+=10
        flag3=0
    if playerX>=pipe4X and flag4 and not gameover:
        score_value+=10
        flag4=0
    player(playerX,playerY)
    pipe(pipeX,pipeY)
    pipe2(pipe2X,pipe2Y)
    pipe3(pipe3X, pipe3Y)
    pipe4(pipe4X, pipe4Y)
    show_score(textX,textY)
    pygame.display.update()
