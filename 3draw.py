import pygame

# 게임스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# 색 정의
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("draw")

# 스크린정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(WHITE)
    pygame.draw.line(screen, RED, [50,50], [500,50], 10)
    pygame.draw.line(screen, GREEN, [50,100], [500,100], 5)
    pygame.draw.line(screen, BLUE, [50,150], [500,150], 20)
    pygame.draw.rect(screen, RED, [50,200,150,150], 3)
    pygame.draw.polygon(screen, GREEN, [[350,200],[250,350],[450,350]],0)
    pygame.draw.circle(screen, BLUE, [150,450], 60, 2)
    pygame.draw.ellipse(screen, BLUE, [250,400,200,100], 0)

    font = pygame.font.SysFont('맑은 고딕', 40, True, False)
    text = font.render("Hello Pygame", True, BLACK)
    screen.blit(text, [200,600])

    pygame.display.flip()
    clock.tick(60)
pygame.quit()