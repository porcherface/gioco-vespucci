
from character import Character

# pygame library, our main library
import pygame
import os
import pathlib

PLAYER_IMG1_PATH = os.path.join(pathlib.Path(__file__).parent.absolute(), "res", "player_asset1.png")
PLAYER_IMG2_PATH = os.path.join(pathlib.Path(__file__).parent.absolute(), "res", "player_asset2.png")

class Pawn(Character):

    def __init__(self, pawn_type):
        Character.__init__(self, pawn_type)
        if pawn_type == "player":
            
            self.image = pygame.image.load(PLAYER_IMG1_PATH)
            self.flipped = pygame.image.load(PLAYER_IMG2_PATH)
            self.rect = self.image.get_rect()
            self.asset = []
            self.asset.append(self.image)
            self.asset.append(self.flipped) 

    def control(self, x, y):
        print("moving "+str(x)+","+str(y))
        self.vx = x
        self.vy = y

    def spell(self, spell_number):
        pass

    # common classes
    def draw(self, world):
        if self.vx < 0:
            world.blit(self.image, self.rect)
        else:
            world.blit(self.flipped, self.rect)
    



    def update(self):
        self.x = self.vx
        self.y = self.vy

        self.rect.move_ip(self.x, self.y)
        self.x = 0
        self.y = 0


# snippet
'''
def point_target_spell(coordis)

def unit_target_spell(unit_id):

def auto_cast_spell():
'''