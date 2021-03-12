import pygame
import random
import time
import threading

pygame.init() 
screen = pygame.display.set_mode((900, 600)) 
pygame.display.set_caption("Genetic Algorithm Covid-19 Simulator")

clock = pygame.time.Clock()
run = True
key = None
start_pos = [450, 300]

x = 1
y = 1
power = False


def move():
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    print("x: " + str(x))
    print("y: " + str(y))

    threading.Timer(0.8, move).start()


# 게임 루프
while run:
    # 1) 사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            key = event.key
            
    # 2) 게임 상태 업데이트    
    if start_pos[0] > screen.get_width():
        start_pos[1] = 300
        start_pos[0] = 450
    if start_pos[1] > screen.get_height():
        start_pos[1] = 300
        start_pos[0] = 450
    else:
        start_pos[0] += x
        start_pos[1] += y
    
    # 3) 게임 상태 그리기
    screen.fill(pygame.color.Color(0, 0, 0))

    if key == pygame.K_2:
            pygame.draw.ellipse(screen,
                pygame.color.Color(255, 0, 0),
                pygame.Rect(start_pos, (10, 10)))
            if power == False:
                power = True
                move()
    
    if key == pygame.K_1:
        x = -1
        y = -1
    
    pygame.display.flip()    
    clock.tick(60)

pygame.quit()