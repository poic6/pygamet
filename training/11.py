import pygame # 1. pygame 선언
 
pygame.init() # 2. pygame 초기화
 
# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255)
size = [400,300]
screen = pygame.display.set_mode(size)
 
done= False
clock= pygame.time.Clock()
 
# pygame에 사용하도록 비행기 이미지를 호출
airplane = pygame.image.load('images/plane.png')
airplane = pygame.transform.scale(airplane, (60, 45))
 
# 4. pygame 무한루프
def runGame():
    global done, airplane
    x = 20
    y = 24
 
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
 
            # 방향키 입력에 대한 이벤트 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 10
                elif event.key == pygame.K_LEFT:
                    x -= 10
                elif event.key == pygame.K_RIGHT:
                    x += 10
    
        screen.blit(airplane, (x, y))
        pygame.display.update()
 
runGame()