import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake!")

#FPS and CLOCK
FPS = 20
clock = pygame.time.Clock()
#game values
SNAKE_SIZE = 20
headX = WINDOW_WIDTH//2
headY = WINDOW_HEIGHT//2 + 100

snakeDx = 0
snakeDy = 0

score = 0


#colors
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
RED = (255,0,0)
DARKRED = (150,0,0)
WHITE = (255,255,255)
#fonts

#text

#sounds

#images
#=============================GAME LOOP===============================
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(WHITE)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()