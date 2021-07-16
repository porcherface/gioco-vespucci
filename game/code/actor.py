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

class Actor(pygame.sprite.Sprite):

    def __init__(self, actor_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.x = 0
        self.y = 0
        self.type = actor_type 
        self.vx = 0
        self.vy = 0