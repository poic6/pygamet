import pygame
import os
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (20, 60, 120)
ORANGE = (250, 170, 70)
RED = (255, 0, 0)

SC_w = 480
SC_h = 640

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")

class Ball():
    """공 객체"""
    def __init__(self, bounce_sound):
        self.rect = pygame.Rect(SC_w//2, SC_h//2, 12, 12)
        self.bounce_sound = bounce_sound
        self.dx = 0
        self.dy = 5
    def update(self):
        """공 업데이트"""
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0:
            self.dx *= -1
            self.rect.left = 0
            self.bounce_sound.play()
        if self.rect.right > SC_w:
            self.dx *= -1
            self.rect.right = SC_w
            self.bounce_sound.play()
    def reset(self, x, y):
        """공 리셋"""
        self.rect.x = x
        self.rect.y = y
        self.dx = random.randint(-3,3)
        self.dy = 5
    def draw(self, screen):
        """공 그리기"""
        pygame.draw.rect(screen, ORANGE, self.rect, 0)

class player():
    """플레이어 객체"""
    def __init__(self, ping_sound):
        self.rect = pygame.Rect(SC_w//2, SC_h-40, 50, 15)
        self.ping_sound = ping_sound
        self.dx = 0
    def update(self, ball):
        """업데이트"""
        if self.rect.left <= 0 and self.dx < 0:
            self.dx = 0
        elif self.rect.right >= SC_w and self.dx > 0:
            self.dx = 0
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5, 5)
            ball.dy *= -1
            ball.rect.bottom = self.rect.top
            self.ping_sound.play()
        self.rect.x += self.dx
    def draw(self, screen):
        """그리기"""
        pygame.draw.rect(screen, RED, self.rect, 0)

class Enemy():
    """적 객체"""
    def __init__(self, pong_sound):
        self.rect = pygame.Rect(SC_w//2, 40, 50, 15)
        self.pong_sound = pong_sound
    def update(self, ball):
        if self.rect.centerx > ball.rect.centerx:
            diff = self.rect.centerx - ball.rect.centerx
            if diff > 4:
                self.rect.x -= 4
            else:
                self.rect.centerx = ball.rect.centerx
        if self.rect.centerx < ball.rect.centerx:
            diff = ball.rect.centerx - self.rect.centerx
            if diff < 4:
                self.rect.x += 4
            else:
                self.rect.centerx = ball.rect.centerx
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5, 5)
            ball.dy *= -1
            ball.rect.top == self.rect.bottom
            self.pong_sound.play()
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect, 0)
    
class Game():
    """게임 객체"""
    def __init__(self):
        bounce_sound = pygame.mixer.Sound(os.path.join(assets_path, "bounce.wav"))
        ping_sound = pygame.mixer.Sound(os.path.join(assets_path, "ping.wav"))
        pong_sound = pygame.mixer.Sound(os.path.join(assets_path, "pong.wav"))
        self.font = pygame.font.SysFont("맑은 고딕", 50, False, False)
        self.ball = Ball(bounce_sound)
        self.player = player(ping_sound)
        self.enemy = Enemy(pong_sound)
        self.player_score = 0
        self.enemy_score = 0

    def process_events(self):
        """게임 이벤트 처리 및 조작"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.dx = -5
                elif event.key == pygame.K_RIGHT:
                    self.player.dx = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.dx = 0
        return True
    def run_logic(self):
        """게임 로직 수행"""
        self.ball.update()
        self.player.update(self.ball)
        self.enemy.update(self.ball)

        if self.ball.rect.top < 0:
            self.player_score += 1
            self.ball.reset(self.player.rect.centerx, self.player.rect.centery-5)
        elif self.ball.rect.bottom > SC_h:
            self.enemy_score += 1
            self.ball.reset(self.enemy.rect.centerx, self.enemy.rect.centery+5)
    def display_message(self, screen, messege, color):
        label = self.font.render(messege, True, color)
        width = label.get_width()
        height = label.get_height()
        pos_x = SC_w//2 - (width//2)
        pos_y = SC_h//2 - (height//2)
        screen.blit(label, (pos_x, pos_y))
        pygame.display.update()
    def display_frame(self, screen):
        screen.fill(BLUE)
        if self.player_score == 10:
            self.display_message(screen, "너 이김ㅋ 좀 하누ㅋㅋ", WHITE)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)
        elif self.enemy_score == 10:
            self.display_message(screen, "너 짐ㅋㅋ 연습하고 와라ㅋ", WHITE)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)
        else:
            self.ball.draw(screen)
            self.player.draw(screen)
            self.enemy.draw(screen)
            
            for x in range(0, SC_w, 24):
                pygame.draw.rect(screen, WHITE, [x, SC_h//2, 10, 10])
            enemy_score_label = self.font.render(str(self.enemy_score), True, WHITE)
            screen.blit(enemy_score_label, (10, 260))
            player_score_label = self.font.render(str(self.player_score), True, WHITE)
            screen.blit(player_score_label, (10, 340))



def main():
    pygame.init()
    pygame.display.set_caption("핑퐁게임")
    screen = pygame.display.set_mode((SC_w, SC_h))
    clock = pygame.time.Clock()
    game = Game()
    running = True
    while running:
        running = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()