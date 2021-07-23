
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
        self.p_dmg = 0
        self.m_dmg = 0

    def behaviour(self):
        pass



class Girilir(Character):
    def __init__(self,char_type):
        Character.__init__(self, char_type)
        self.hp = 372
        self.armor = 19
        self.magic_res = 17
        self.agi = 31
        self.p_dmg = 13
        self.m_dmg = 24
        self.padronance = 20

    def behaviour(self):
        pass


    def fuffa(self):
        print("fuffo2")

    def draw(self):
        pass