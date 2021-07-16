# -*- coding: utf-8 -*-

# a signature
doggo ='''
                   ▄              ▄
                  ▌▒█           ▄▀▒▌
    WOW           ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌  MUCH GAME
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐ SUCH MOBA
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
VERY RPG    ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
                   ▒▒▒▒▒▒▒▒▒▒▀▀ 
'''


###################################################
#                                                 #
# project name: HeN                               #
# author: riccardo, simone, andrea                #
#                                                 #
#                                                 #
#                                                 #
###################################################

# our game imports
from actor import Actor, Totem, Tree
from character import Character
from pawn import Pawn

# pygame library, our main library
import pygame
import os
import pathlib
import sys

MAIN_PATH = pathlib.Path(__file__).parent.absolute()
FPS = 40
clock =  pygame.time.Clock()
# game initialization
pygame.init()
pygame.display.init()
pygame.mixer.init()

# resolution and game screen 
RES_X = 1280
RES_Y = 1080

screen = pygame.display.set_mode([RES_X, RES_Y])

background_path = os.path.join(MAIN_PATH,"res", "back_map.png")
background = pygame.image.load(background_path)
back_rect  = background.get_rect()


# we spawn a player: 
player = Pawn("player")
totem = Totem("totem")
totem.place(400,400)

# tree placing
trees = []
trees.append(Tree("tree",100,120))
trees.append(Tree("tree",300,220))
trees.append(Tree("tree",140,420))
trees.append(Tree("tree",550,560))
trees.append(Tree("tree",1200,120))


#a simple game loop
n = 0

# functions and events
def render():

    # image blits
    screen.blit(background, back_rect)
    
    for tree in trees:
        tree.draw(screen)

    totem.draw(screen)
    player.draw(screen)
    # screen flip: draws all the blits
    pygame.display.flip()
    pygame.display.update()

def update():
    player.update()
    totem.update()

step = 9

def handle_events(events):
        for event in events:
 
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key == ord('a'):
                    player.control(-step, 0)
              
                if event.key == ord('d'):
                    player.control(step, 0)
               
                if event.key == ord('w'):
                    player.control(0,-step)
                 
                if event.key == ord('s'):
                    player.control(0,step)
                
                if event.key == ord('q'):
                    player.spell(1)
                
                if event.key == ord('e'):
                    player.spell(2)

                if event.key == ord(' '):
                    player.control(0, 0)

while "forever":

    handle_events(pygame.event.get())
    update()
    render()
    clock.tick(FPS)

# main code 
if __name__ == "__main__":
    pass












