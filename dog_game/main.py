import pygame
from pygame.locals import *

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

dog_right = pygame.transform.flip(dog, True, False)
dog_left = dog

DOG_NORMAL_VELOCITY = 5
DOG_BOOST_VELOCITY = 15
velocity = DOG_NORMAL_VELOCITY
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dog_rect.x -= velocity
        dog = dog_left
    if keys[pygame.K_RIGHT]:
        dog_rect.x += velocity
        dog = dog_right

    if keys[K_UP]:
        dog_rect.y -= velocity
    if keys[K_SPACE]:
        velocity = DOG_BOOST_VELOCITY
    else:
        velocity = DOG_NORMAL_VELOCITY
    
    screen.fill((0,0,0))
    screen.blit(dog,dog_rect)
    pygame.display.update()
    clock.tick(FPS)