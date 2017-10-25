import pygame
import sys
sys.path.append("../")

colors = ["red", "green", "blue", "white"]

class Tank:
    def __init__(self, _id=0, posx=0, posy=0, rot=0, aim=0, speed=5):
        self.id = _id
        self.posx = posx
        self.posy = posy
        self.rot = rot
        self.aim = aim
        self.speed = speed
        
    def setup(self):
        self.body = pygame.image.load("/assets/pictures/tank_{}_bottom.png".format(colors[self.id]))
        self.turret = pygame.image.load("/assets/pictures/tank_{}_top.png".format(colors[self.id]))
    
    def draw(self):
        pass