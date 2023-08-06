# 흰화면 기본코드
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

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
    pygame.draw.rect(screen, BLACK, [50,50,100,100], 0)
    pygame.draw.rect(screen, BLUE, [SCREEN_WIDTH//2,SCREEN_HEIGHT//2, 50,50], 0)

    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()