import pygame
from color import color

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

FPS = 60

class Ball():
    def __init__(self, bounce_sound):
        self.rect = pygame.Rect(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), 12, 12)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pingpong Game")
    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(color('WHITE'))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()