import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255,255,255)

pygame.init()

pygame.display.set_caption("Test Pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("맑은 고딕", 50, False, False)

running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    screen.fill(WHITE)
    hello = font.render("Hello", False, WHITE)
    screen.blit(hello, (50, 50))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()