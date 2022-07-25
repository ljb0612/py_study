from ctypes.wintypes import POINT
from secrets import token_hex
import pygame
from random import *

##############################################################################################
# 기본 초기화 (무조건 해야 하는 부분)
pygame.init()   # 초기화 (무조건 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 title
pygame.display.set_caption("Game Test")

# FPS
clock = pygame.time.Clock()
##############################################################################################

# 1. 사용자 게임 초기화 (배경화면, 이미지, 좌표, 폰트 등)

#bg = pygame.image.load("C:\\py_study\\basic\\py_study\\pygame_basic\\bg.png")
bg = pygame.image.load("./pygame_basic/bg.png")
char = pygame.image.load("./pygame_basic/character.png")
enemy = pygame.image.load("./pygame_basic/enemy.png")

char_width = char.get_width()
char_height = char.get_height()
char_x = screen_width / 2 - char_width / 2
char_y = screen_height - char_height

enemy_width = enemy.get_width()
enemy_height = enemy.get_height()
enemy_x = randrange(0,screen_width-char_width+1)
enemy_y = 0
to_x = 0

speed = 0.5
ddong_speed = 0.5

text_font = pygame.font.Font(None,30)

running = True
isExistDD = False

while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed
            if event.key == pygame.K_RIGHT:
                to_x += speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    
    # 3. 게임 캐릭터 위치 정의
    
    # enemy 좌표
    char_x += to_x * dt
    enemy_y += ddong_speed * dt
    
    # 4. 충돌 처리

    # 경계
    if char_x < 0:
        char_x = 0
    if char_x > screen_width - char_width:
        char_x = screen_width - char_width

    # 충돌 계산
    char_rc = char.get_rect()
    char_rc.left = char_x
    char_rc.top = char_y
    enemy_rc = enemy.get_rect()
    enemy_rc.left = enemy_x
    enemy_rc.top = enemy_y

    # 충돌 체크
    if char_rc.colliderect(enemy_rc):
        running = False

    if enemy_rc.top >= screen_height:
        enemy_y = 0
        enemy_x = randrange(0,screen_width-char_width+1)

    # 5. 화면에 그리기
    screen.blit(bg,(0,0))
    screen.blit(char,(char_x,char_y))
    screen.blit(enemy,(enemy_x,enemy_y))
    
    pygame.display.update()     # redraw

# 종료직전 대기
pygame.time.delay(500)

# pygame 종료
pygame.quit()