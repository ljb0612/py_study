import pygame

pygame.init()   # 초기화 (무조건 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 title
pygame.display.set_caption("Game Test")

# 배경 이미지 불러오기
bg = pygame.image.load("C:\\py_study\\basic\\py_study\\pygame_basic\\bg.png")

# 스프라이트 불러오기
character = pygame.image.load("C:\\py_study\\basic\\py_study\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x = screen_width / 2 - (character_width / 2)
character_y = screen_height - character_height

# event loop
running = True
while running:
    for event in pygame.event.get():    # 무조건 필요 (마우스,키보드 이벤트 체크)
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg,(0,0))
    screen.blit(character,(character_x,character_y))
    pygame.display.update()     # redraw

# pygame 종료
pygame.quit()