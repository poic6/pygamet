import pygame
import color

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.displya.set_caption("Pingpong Game")
    clock = pygame.time.Clock()

    done = False
    while not done:
        done = game.process_events()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()