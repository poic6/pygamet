import pygame
import os
import sys
import random
import math
from time import sleep

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0,0,0)
WHITE = (200,200,200)
YELLOW = (250,250,20)
BLUE = (20,20,250)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()
        spaceship_image_path = resource_path('assets/spaceship.png')
        explosion_image_path = resource_path('assets/explosion.png')
        explosion_sound_path = resource_path('assets/explosion.wav')
        self.image = pygame.image.load(spaceship_image_path)
        self.explosion_image = pygame.image.load(explosion_image_path)
        self.explosion_sound = pygame.mixer.Sound(explosion_sound_path)
        self.rect = self.image.get_rect()
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
    def set_pos(self, x, y):
        self.rect.x = x-self.centerx
        self.rect.y = y-self.centery
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
    def occur_explosion(self, screen):
        explosion_rect = self.explosion_image.get_rect()
        explosion_rect.x = self.rect.x
        explosion_rect.y = self.rect.y
        screen.blit(self.explosion_image, explosion_rect)
        pygame.display.update()
        self.explosion_sound.play()

class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Rock, self).__init__()
        rock_images_path = resource_path('assets/rock')
        image_file_list = os.listdir(rock_images_path)
        self.image_path_list = [os.path.join(rock_images_path, file) for file in image_file_list if file.endswith(".png")]
        choice_rock_path = random.choice(self.image_path_list)
        self.image = pygame.image.load(choice_rock_path)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed
        self.set_direction()
    def set_direction(self):
        if self.hspeed > 0:
            self.imgae = pygame.transform.rotate(self.image, 270)
        elif self.hspeed < 0:
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.vspeed > 0:
            self.image = pygame.transform.rotate(self.image, 180)
    def update(self):
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed

class Warp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Warp, self).__init__()
        self.image = pygame.image.load(resource_path('assets/warp.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x-self.rect.centerx
        self.rect.y = y-self.rect.centery

class Game():
    def __init__(self):
        self.menu_image = pygame.image.load(resource_path('assets/game_screen.png'))
        self.background_image = pygame.image.load(resource_path('assets/background.jpg'))
        self.font_70 = pygame.font.SysFont("Malgun Gothic", 70)
        self.font_30 = pygame.font.SysFont("Malgun Gothic", 30)
        self.warp_sound = pygame.mixer.Sound(resource_path('assets/warp.wav'))
        pygame.mixer.music.load('assets/Inner_Sanctum.mp3')

        self.spaceship = Spaceship()
        self.rocks = pygame.sprite.Group()
        self.warps = pygame.sprite.Group()

        self.occur_prob = 15
        self.score = 0
        self.warp_count = 1
        self.menu_on = True
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.menu_on:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                    self.score = 0
                    self.warp_count = 1
                    self.menu_on = False
            else:
                if event.type==pygame.MOUSEMOTION:
                    self.spaceship.set_pos(*pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.warp_count>0:
                        self.warp_count -= 1
                        self.warp_sound.play()
                        sleep(1)
                        self.rocks.empty()
        return True
    def run_logic(self, screen):
        occur_of_rocks = 1+self.score//500
        min_rock_speed = 1+self.score//400
        max_rock_speed = 1+self.score//300

        if random.randint(1, self.occur_prob) == 1:
            for i in range(occur_of_rocks):
                self.rocks.add(self.create_random_rock(min_rock_speed, max_rock_speed))
                self.score += 1
        if random.randint(1, self.occur_prob*10) == 1:
            warp = Warp(random.randint(30, SCREEN_WIDTH-30),random.randint(40, SCREEN_HEIGHT-30))
            self.warps.add(warp)
        if self.spaceship.collide(self.rocks):
            pygame.mixer.music.stop()
            self.spaceship.occur_explosion(screen)
            self.rocks.empty()
            self.menu_on = True
            sleep(1)
        
        warp = self.spaceship.collide(self.warps)
        if warp:
            self.warp_count += 1
            warp.kill()

    def create_random_rock(self, min_rock_speed, max_rock_speed):
        direction = random.randint(1,4)
        speed = random.randint(min_rock_speed, max_rock_speed)
        if direction ==1:
            return Rock(random.randint(0, SCREEN_WIDTH), 0, 0, speed)
        elif direction ==2:
            return Rock(SCREEN_WIDTH, random.randint(0,SCREEN_HEIGHT),-speed, 0)
        elif direction ==3:
            return Rock(random.randint(0,SCREEN_WIDTH), SCREEN_HEIGHT, 0, -speed)
        elif direction == 4:
            return Rock(0, random.randint(0, SCREEN_HEIGHT), speed, 0)
    def draw_background(self, screen):
        background_rect = self.background_image.get_rect()
        for i in range(int(math.ceil(SCREEN_WIDTH/background_rect.width))):
            for j in range(int(math.ceil(SCREEN_HEIGHT/background_rect.height))):
                rect = pygame.Rect(i*background_rect.width, j*background_rect.height, background_rect.width, background_rect.height)
                screen.blit(self.background_image, rect)
    def draw_text(self, screen, text, font, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.center = x, y
        screen.blit(text_obj, text_rect)
    def display_menu(self, screen):
        pygame.mouse.set_visible(True)
        screen.blit(self.menu_image, [0,0])
        draw_x = SCREEN_WIDTH // 2
        draw_y = SCREEN_HEIGHT // 4
        self.draw_text(screen, '우주암석 피하기', self.font_70, draw_x, draw_y, WHITE)
        self.draw_text(screen, "점수: {}".format(self.score), self.font_30, draw_x, draw_y+100, YELLOW)
        self.draw_text(screen, "press mouse button to start game", self.font_30, draw_x, draw_y+180, WHITE)
    def display_frame(self, screen):
        self.draw_background(screen)
        screen.blit(self.spaceship.image, self.spaceship.rect)
        self.draw_text(screen, "점수: {}".format(self.score), self.font_30, 80, 20, YELLOW)
        self.draw_text(screen,  '워프: {}'.format(self.warp_count), self.font_30, 700, 20, BLUE)
        self.rocks.update()
        self.warps.update()
        self.rocks.draw(screen)
        self.warps.draw(screen)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def main():
    pygame.init()
    pygame.display.set_caption("우주선 게임")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while running:
        running = game.process_events()
        if game.menu_on:
            game.display_menu(screen)
        else:
            game.run_logic(screen)
            game.display_frame(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
main()