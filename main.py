#this file was created by Marcus Ponce
#thanks Chris Bradfield from Kids Can Code

import pygame as pg
import random
from settings import *
from sprites import * 

class Game:
    def __init__(self):
        #init game window, try:
        pg.init()
        pg.mixer.init()
        self.screen = pg.displau.set_mode(WIDTH, HEIGHT)
        pg.display.set_caption 
        self.clock = pg.time.Clock()
        self.running = True
        
        #init pygame and create
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        #create new player object
    def run(self):
        
        #game loop
    def update(self):
        
        #updates things
    def events(self):
        pass
        #listening for events
    def draw(self):
        pass
        #
    def show_start_screen(self):
        pass
        #
    def show_go_screen(self): 
        pass
        #
    
game = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()