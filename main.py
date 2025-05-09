import pygame
import random

pygame.init()

height,width = 600,800
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Adventure game")

# colors
WHITE = (255,255,255)

clock = pygame.time.Clock()
FPS = 60

player_image = pygame.image.load("player.png").convert_alpha()
bg = pygame.image.load('bg.png').convert()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

player = Player(100, 100, 5)
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player
    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    # Draw everything
    window.fill(WHITE)
    all_sprites.draw(window)
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()