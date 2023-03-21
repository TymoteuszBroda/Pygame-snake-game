import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake!")

#=============================GAME LOOP===============================
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(255,255,255)
    pygame.display.update()