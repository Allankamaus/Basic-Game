import pygame
from sprites import *
from config import *
import sys

pygame.init()

height,width = 600,800


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((height,width))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Comicsans.ttf', 32)
        self.running = True


window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Adventure game")

# colors
WHITE = (255,255,255)

clock = pygame.time.Clock()
FPS = 60

player_image = pygame.image.load("player.png").convert_alpha()
bg = pygame.image.load('bg.png').convert()


#enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = enemy_image

def new(self):
    self.playing = True
    self.all_sprites = pygame.sprite.LayeredUpdates()
    self.blocks = pygame.sprite.LayeredUpdates()
    self.enemies = pygame.sprite.LayeredUpdates()
    self.attacks = pygame.sprite.LayeredUpdates()
    self.player = Player()


#empty functions
# def update(self):

# def draw(self):

# def main(self):

# def game_over(self):

# def intro_screen(self):
#load backgroud
bg = pygame.transform.scale(bg, (width, height))            

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
    window.blit(bg, (0, 0))
    all_sprites.update(keys)

    # Draw everything
    
    all_sprites.draw(window)
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()