import pygame
from config import *
import math
import random


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, game,x, y, speed):
        super().__init__()
        self.game = game
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
