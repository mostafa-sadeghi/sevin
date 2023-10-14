import pygame
pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wolf Game")
wolf = pygame.image.load("wolf_game/wolf.png")
pygame.display.set_icon(wolf)


wolf_rect = wolf.get_rect()
wolf_rect.bottom = SCREEN_HEIGHT
wolf_rect.right = SCREEN_WIDTH



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(wolf, wolf_rect)
    
    pygame.display.update()
