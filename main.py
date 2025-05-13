import pygame
from sprites import *
from config import *
import sys

pygame.init()

# colors
WHITE = (255,255,255)

clock = pygame.time.Clock()
FPS = 60

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Adventure game")


# player_image = pygame.image.load("player.png").convert_alpha()
# bg = pygame.image.load('bg.png').convert()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((height,width))
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font( 32)
        self.running = True


    def new(self):
            self.playing = True
            self.all_sprites = pygame.sprite.LayeredUpdates()
            self.blocks = pygame.sprite.LayeredUpdates()
            self.enemies = pygame.sprite.LayeredUpdates()
            self.attacks = pygame.sprite.LayeredUpdates()
    
            self.player = Player(self,1,2)
            self.all_sprites.add(self.player) 


#empty functions
    def events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False

    def update(self,keys):
            self.all_sprites.update()

    def draw(self):
            self.screen.fill(WHITE)
            self.all_sprites.draw(self.screen)
            self.clock.tick(FPS)
            pygame.display.update()

    def main(self):
            while self.playing:
                self.events()
                self.update()
                self.draw()
            self.running = False

    def game_over(self):
            pass

    def intro_screen(self):
            pass



g =Game()
g.intro_screen()
g.new()

#load backgroud
# bg = pygame.transform.scale(bg, (width, height))            

# player = Player(100, 100, 5)
# all_sprites = pygame.sprite.Group(player)

running = True
while running:
    g.main()
    g.game_over()
#     clock.tick(FPS)

#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Update player
#     keys = pygame.key.get_pressed()
#     window.blit(bg, (0, 0))
#     all_sprites.update(keys)

#     # Draw everything
    
#     all_sprites.draw(window)
#     pygame.display.flip()

# # Clean up
pygame.quit()
sys.exit()