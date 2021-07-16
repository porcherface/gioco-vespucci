
from actor import Actor

# pygame library, our main library
import pygame
import os
import pathlib

class Character(Actor):

    def __init__(self,char_type):
        Actor.__init__(self, char_type)
        self.hp = -1
        self.hp_regen = -1
        self.armor = 0
        self.magic_res = 0
        self.padronance = 0
        self.agi = 0
