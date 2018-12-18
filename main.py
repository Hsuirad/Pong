import pygame
import random
import time

pygame.init()

HEIGHT = 600
WIDTH = 800

black = (0, 0, 0)
white = (255, 255, 255)

disp = pygame.display.set_mode((WIDTH, HEIGHT))

disp.fill(black)

clock = pygame.time.Clock()

def firstpaddle(y):
    pygame.draw.rect(disp, white, (20, y, 20, 120))

def secondpaddle(y):
    pygame.draw.rect(disp, white, (750, y, 20, 120))

def ball(x, y):
    pygame.draw.rect(disp, white, (x, y, 20, 20))

def scorecounter(firstscore, secondscore):
    large_text = pygame.font.SysFont("sdfsd", 30)
    textr = large_text.render("Score: " + str(firstscore) + " : " + str(secondscore), True, white)
    disp.blit(textr, (340, 20))

def game_loop():
    play = True

    ball_x = 380
    ball_y = 280
    bx_change = 0
    by_change = 0

    firstscore = 0
    secondscore = 0

    firstx = 20
    firsty = 20
    fy_change = 0

    bx_modifier = 1
    by_modifier = 1

    secondx = 750
    secondy = 20
    sy_change = 0

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    fy_change = -5
                elif event.key == pygame.K_s:
                    fy_change = 5
                if event.key == pygame.K_DOWN:
                    sy_change = 5
                elif event.key == pygame.K_UP:
                    sy_change = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    fy_change = 0
                elif event.key == pygame.K_s:
                    fy_change = 0
                if event.key == pygame.K_DOWN:
                    sy_change = 0
                elif event.key == pygame.K_UP:
                    sy_change = 0

        firsty += fy_change
        secondy += sy_change
        ball_x += bx_change
        ball_y += by_change

        if by_change == 0:
            chance = random.randint(0, 1)
            if chance == 0:
                by_change = -1 * by_modifier
            else:
                by_change = 1 * by_modifier
        if bx_change == 0:
            chance = random.randint(0, 1)
            if chance == 0:
                bx_change = -1 * bx_modifier
            else:
                bx_change = 1 * bx_modifier

        if ball_y >= 580:
            by_change = -1 * by_modifier
        if ball_y <= 0:
            by_change = 1 * by_modifier
        if ball_x >= 780:
            firstscore += 1
            ball_x = 380
            ball_y = 280
            bx_change = 1
            by_change = 1
            bx_modifier = 1
            by_modifier = 1
            time.sleep(1)
        if ball_x <= 20:
            secondscore += 1
            ball_x = 380
            ball_y = 280
            bx_change = 1
            by_change = 1
            bx_modifier = 1
            by_modifier = 1
            time.sleep(1)
        if ball_x <= firstx + 20:
            if firsty <= ball_y <= firsty + 120:
                bx_change = 1 * bx_modifier
                '''if by_change == 1:
                    by_change = -1
                else:
                    by_change = 1'''
        if ball_x + 20 >= secondx:
            if secondy <= ball_y <= secondy + 120:
                bx_change = -1 * bx_modifier
                '''if by_change == 1:
                    by_change = -1
                else:
                    by_change = 1'''

        bx_modifier += 0.003
        by_modifier += 0.003

        disp.fill(black)
        firstpaddle(firsty)
        secondpaddle(secondy)
        ball(ball_x, ball_y)
        scorecounter(firstscore, secondscore)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
