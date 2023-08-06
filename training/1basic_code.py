# 흰화면 기본코드
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255,255,255)

pygame.init()

pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()