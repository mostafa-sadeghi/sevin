from random import randint
import pygame
pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
score = 0


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wolf Game")
wolf = pygame.image.load("wolf_game/wolf.png")
wolf = pygame.transform.scale(wolf, (128, 128))
pygame.display.set_icon(wolf)

pygame.mixer.music.load("wolf_game/bgmusic.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

catch_sound = pygame.mixer.Sound("wolf_game/Chomp.wav")


wolf_rect = wolf.get_rect()
wolf_rect.bottom = SCREEN_HEIGHT
wolf_rect.right = SCREEN_WIDTH

sheep = pygame.image.load("wolf_game/sheep.png")
sheep = pygame.transform.flip(sheep, True, False)
sheep_rect = sheep.get_rect()
sheep_rect.topleft = (0, randint(100, SCREEN_HEIGHT - 48))


font = pygame.font.Font("wolf_game/font.otf", 48)
title = font.render("Wolf game", True, (255, 84, 0, 1))
title_rect = title.get_rect()
title_rect.top = 0
title_rect.centerx = SCREEN_WIDTH/2

score_text = font.render(f'Score: {score}', True, (255, 0, 0))
score_rect = score_text.get_rect()
score_rect.topleft = (0, 0)


FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and wolf_rect.top > 0:
        wolf_rect.y -= 5
    if keys[pygame.K_DOWN] and wolf_rect.bottom < SCREEN_HEIGHT:
        wolf_rect.y += 5

    sheep_rect.x += 5
    if sheep_rect.x > SCREEN_WIDTH:
        sheep_rect.topleft = (0, randint(100, SCREEN_HEIGHT - 48))

    if wolf_rect.colliderect(sheep_rect):
        score += 1
        catch_sound.play()
        sheep_rect.topleft = (0, randint(100, SCREEN_HEIGHT - 48))

    score_text = font.render(f'Score: {score}', True, (255, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(wolf, wolf_rect)
    screen.blit(sheep, sheep_rect)
    screen.blit(title, title_rect)
    screen.blit(score_text, score_rect)

    pygame.display.update()
    clock.tick(FPS)
