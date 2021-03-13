import sys
sys.path.append("/Users/xiaoqiongzhang/anaconda3/lib/python3.7/site-packages")

import pygame
import time as t

import random
from pygame import *



redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)
greyColor = pygame.Color(150,150,150)

# Game Over
def gameOver(playSurface,score):
    
    gameOverFont = pygame.font.SysFont("arial.ttf",50) # Font and Size
    gameOverSurf = gameOverFont.render("Game Over!",True,greyColor)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (300,10) # show the location
    playSurface.blit(gameOverSurf,gameOverRect)

    scoreFont = pygame.font.SysFont("arial.ttf",50) # Font and Size
    scoreSurf = scoreFont.render("Score:"+str(score),True,greyColor)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (300,50) # show the location
    playSurface.blit(scoreSurf,scoreRect)

    pygame.display.update()
    t.sleep(5)
    pygame.quit()
    sys.exit()


def main():
    # Initialization
    pygame.init()
    clock = pygame.time.Clock()
    
    # Display
    playSurface = pygame.display.set_mode((600,460)) #size of window
    pygame.display.set_caption("Greedy Snake Game")
    
    
    # Initialization
    snakePosition = [100,100]
    snakeSegments = [[100,100]]
    raspberryPosition = [300,300]
    raspberryNum = 1
    direction = "Not Given"
    changeDirection = direction
    score = 0
    
    # Control Path of Snake
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over == True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT or event.key == ord("d"):
                    changeDirection = "right"
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    changeDirection = "left"
                if event.key == pygame.K_UP or event.key == ord("w"):
                    changeDirection = "up"
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    changeDirection = "down"
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        # Based on the rule, we cannot change the movement to opposite direction
        if changeDirection == "right" and not direction == "left":
            direction = changeDirection
        if changeDirection == "left" and not direction == "right":
            direction = changeDirection
        if changeDirection == "up" and not direction == "down":
            direction = changeDirection
        if changeDirection == "down" and not direction == "up":
            direction = changeDirection

        # Change the direction of snake movement
        if direction == "right":
            snakePosition[0] += 20
        if direction == "left":
            snakePosition[0] -= 20
        if direction == "up":
            snakePosition[1] -= 20
        if direction == "down":
            snakePosition[1] += 20
        snakeSegments.insert(0,list(snakePosition))
        
        # Eat Raspberry or not
        if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
            raspberryNum = 0
        else:
            snakeSegments.pop()
        
        if raspberryNum == 0:
            x = random.randrange(1,30)
            y = random.randrange(1,23)
            raspberryPosition = [int(x*20),int(y*20)]
            raspberryNum = 1
            score += 1

        # Died or not
        if snakePosition[0] > 600 or snakePosition[0] < 0: #out
            gameOver(playSurface,score)
            gameOver == True
        if snakePosition[1] > 460 or snakePosition[1] < 0: #out
            gameOver(playSurface,score)
            gameOver == True
        for snakeBody in snakeSegments[1:]: #touch itself
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface,score)
                gameOver == True
        
        # Update display and speed
        playSurface.fill(blackColor)
        for position in snakeSegments:
            pygame.draw.rect(playSurface,whiteColor,Rect(position[0],position[1],20,20))
            pygame.draw.rect(playSurface,redColor,Rect(raspberryPosition[0],raspberryPosition[1],20,20))

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()


main()
