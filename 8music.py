import pygame
import os

# 게임스크린 크기
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400

# 색 정의
BLACK = (0,0,0)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("sound")

# 스크린정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임화면 업데이트 속도
clock = pygame.time.Clock()

# 불러오기
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

background_image = pygame.image.load(os.path.join(assets_path, 'equalizer.png'))
pygame.mixer.music.load(os.path.join(assets_path, 'bgm.wav'))
pygame.mixer.music.play(-1)

sound = pygame.mixer.Sound(os.path.join(assets_path, 'sound.wav'))

# 게임 종료 전까지 반복
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()
            
    screen.fill(BLACK)

    screen.blit(background_image, background_image.get_rect())
    pygame.display.flip()
    clock.tick(60)
pygame.quit()