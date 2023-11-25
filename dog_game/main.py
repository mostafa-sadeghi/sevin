import random
import pygame
from pygame.locals import *
pygame.init()
screen_width = 1000
screen_height = 700
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("dog game")
clock = pygame.time.Clock()

# load dog image
dog = pygame.image.load("dog.png")
dog = pygame.transform.scale(dog, (96,96))
dog_rect = dog.get_rect()
dog_rect.bottom = screen_height
dog_rect.centerx = screen_width/2

# load sheep image
sheep = pygame.image.load("sheep.png")
sheep = pygame.transform.scale(sheep, (36,36))
sheep_rect = sheep.get_rect()
sheep_rect.top = 100
sheep_rect.centerx = random.randint(sheep.get_width()/2,screen_width-sheep.get_width()/2)

# define sheep velocity
SHEEP_NORMAL_VELOCITY = 5
sheep_velocity = SHEEP_NORMAL_VELOCITY


pygame.display.set_icon(dog)
font72 = pygame.font.Font("font.otf", 72)
font24 = pygame.font.Font("font.otf", 24)
score = 0
lives = 3
START_BOOST = 100
boost = START_BOOST
SHEEP_START_POINTS = 100
sheep_point = SHEEP_START_POINTS

score_text = font24.render(f'Score {score}', True, (245, 17, 189))
score_rect = score_text.get_rect(topleft=(10,10))
lives_text = font24.render(f'Lives {lives}', True, (245, 17, 189))
lives_rect = lives_text.get_rect(topright=(screen_width,10))

boost_text = font24.render(f'boost {boost}', True, (245, 17, 189))
boost_rect = boost_text.get_rect(topleft=(10,40))
sheep_point_text = font24.render(f'sheep points {sheep_point}', True, (245, 17, 189))
sheep_point_rect = sheep_point_text.get_rect(topright=(screen_width,40))

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
    if keys[pygame.K_LEFT] and dog_rect.left > 0:
        dog_rect.x -= velocity
        dog = dog_left
    if keys[pygame.K_RIGHT] and dog_rect.right < screen_width:
        dog_rect.x += velocity
        dog = dog_right

    if keys[K_UP] and dog_rect.top > 100:
        dog_rect.y -= velocity
    if keys[K_DOWN] and dog_rect.bottom < screen_height:
        dog_rect.y += velocity
    if keys[K_SPACE] and boost > 0:
        boost -= 1
        velocity = DOG_BOOST_VELOCITY
    else:
        velocity = DOG_NORMAL_VELOCITY
    
    sheep_rect.y += sheep_velocity
    if sheep_rect.top >= screen_height:
        sheep_rect.top = 100
        sheep_rect.centerx = random.randint(sheep.get_width()/2,screen_width-sheep.get_width()/2)
        sheep_point = SHEEP_START_POINTS
    
    if dog_rect.colliderect(sheep_rect):
        sheep_rect.top = 100
        sheep_rect.centerx = random.randint(sheep.get_width()/2,screen_width-sheep.get_width()/2)
        score += sheep_point

    sheep_point = (screen_height - sheep_rect.y)//100 + 1
    score_text = font24.render(f'Score {score}', True, (245, 17, 189))
    boost_text = font24.render(f'boost {boost}', True, (245, 17, 189))
    sheep_point_text = font24.render(f'sheep points {sheep_point}', True, (245, 17, 189))
    screen.fill((0,0,0))
    screen.blit(dog,dog_rect)
    screen.blit(sheep,sheep_rect)
    screen.blit(score_text, score_rect)
    screen.blit(lives_text, lives_rect)
    screen.blit(boost_text, boost_rect)
    screen.blit(sheep_point_text, sheep_point_rect)
    pygame.display.update()
    clock.tick(FPS)