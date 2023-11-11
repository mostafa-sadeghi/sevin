import pygame

screen_width = 1000
screen_height = 700
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


dog = pygame.image.load("dog.png")
dog = pygame.transform.scale(dog, (96,96))
dog_rect = dog.get_rect()
dog_rect.bottom = screen_height
dog_rect.centerx = screen_width/2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dog_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        dog_rect.x += 5
    screen.fill((0,0,0))
    screen.blit(dog,dog_rect)
    pygame.display.update()
    clock.tick(FPS)