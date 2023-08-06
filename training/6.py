# 흰화면 기본코드
import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255, 0, 0)
GREEN = (0,255,0)

pygame.init()

pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

rect1 = pygame.Rect(0, 0, 100, 100)
rect1.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
color = BLACK

running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color = random.choice([BLUE, RED, GREEN])

    screen.fill(WHITE)
    
    pygame.draw.rect(screen, color, rect1)


    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()