import pygame, random

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
font = pygame.font.SysFont("gabriela", 48)
#text
titleText = font.render("Snake", True, GREEN, DARKRED)
titleRect = titleText.get_rect()
titleRect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

scoreText = font.render(f"Score: {score}", True, GREEN, DARKRED)
scoreRect = scoreText.get_rect()
scoreRect.topleft = (10,10)

gameOverText = font.render("Game Over!", True, RED, DARKGREEN)
gameOverRect = gameOverText.get_rect()
gameOverRect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continueText = font.render("Press any key to play again", True, RED, DARKGREEN)
continueRect = continueText.get_rect()
continueRect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)
#sounds
pickUpSound = pygame.mixer.Sound("pick_up_sound.wav")

#images
appleCoord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
headCoord = (headX, headY, SNAKE_SIZE, SNAKE_SIZE)
bodyCoords = []


appleRect = pygame.draw.rect(window, RED, appleCoord)
headRect = pygame.draw.rect(window, GREEN, headCoord)

#=============================GAME LOOP===============================
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #Move snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                snakeDx = -SNAKE_SIZE
                snakeDy = 0
            if event.key == pygame.K_d:
                snakeDx = SNAKE_SIZE
                snakeDy = 0
            if event.key == pygame.K_w:
                snakeDx = 0
                snakeDy = -SNAKE_SIZE
            if event.key == pygame.K_s:
                snakeDx = 0
                snakeDy = SNAKE_SIZE
                
    #update position of snake head
    headX += snakeDx
    headY += snakeDy
    headCoord = (headX, headY, SNAKE_SIZE, SNAKE_SIZE)
    
    #collision check
    if headRect.colliderect(appleRect):
        score+=1
        pickUpSound.play()
        
        appleX = random.randint(0, WINDOW_WIDTH-SNAKE_SIZE)
        appleY = random.randint(0, WINDOW_HEIGHT-SNAKE_SIZE)
        appleCoord = (appleX, appleY, SNAKE_SIZE, SNAKE_SIZE)
    
        
    window.fill(WHITE)
    #HUD
    window.blit(titleText, titleRect)
    window.blit(scoreText, scoreRect)
    
    #assets
    headRect = pygame.draw.rect(window, GREEN, headCoord)
    appleRect = pygame.draw.rect(window, RED, appleCoord)
    
    #HUD update
    scoreText = font.render(f"Score: {score}", True, GREEN, DARKGREEN)
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()