import pygame
from config import *
import math
import random


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, game,x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((RED))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.topleft = (x, y)
        

    def update(self):
        # if keys[pygame.K_LEFT]:
        #     self.rect.x -= self.speed
        # if keys[pygame.K_RIGHT]:
        #     self.rect.x += self.speed
        # if keys[pygame.K_UP]:
        #     self.rect.y -= self.speed
        # if keys[pygame.K_DOWN]:
        #     self.rect.y += self.speed
        pass
