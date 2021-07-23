###################################################
#                                                 #
#    game design @ vespucci                       #
#    author: porcherface                          #
#    file desc: actor class                       #
#                                                 #
#                                                 #
###################################################

# pygame library, our main library
import pygame
import os
import pathlib

TOTEM_IMG_PATH = os.path.join(pathlib.Path(__file__).parent.absolute(), "res", "totem_asset.png")
TREE_IMG_PATH = os.path.join(pathlib.Path(__file__).parent.absolute(), "res", "tree_asset.png")


class Actor(pygame.sprite.Sprite):

    def __init__(self, actor_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.x = 0
        self.y = 0
        self.type = actor_type 
        self.vx = 0
        self.vy = 0

    # common classes
    def draw(self, world):
        world.blit(self.image, self.rect)

    def update(self):
        pass

    def place(self, x, y):
        self.x = x 
        self.y = y
        self.rect.move_ip(x,y)


class Totem(Actor):

    def __init__(self, pawn_type = "totem",x = 0, y = 0):
        Actor.__init__(self, pawn_type)
        if pawn_type == "totem":
            self.image = pygame.image.load(TOTEM_IMG_PATH)
            self.rect = self.image.get_rect()
        self.place(x,y)
 
class Tree(Actor):
    def __init__(self, pawn_type = "tree", x = 0, y = 0):
        Actor.__init__(self, pawn_type)
        if pawn_type == "tree":
            self.image = pygame.image.load(TREE_IMG_PATH)
            self.rect = self.image.get_rect()
        self.place(x,y)
        
 