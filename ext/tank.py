import pygame
import sys, os
from collections import namedtuple
sys.path.append("../")

colors = ["red", "green", "blue", "white"]
Position = namedtuple("Position", ["x","y"])

class Tank:
    def __init__(self, _id=0, pos=Position(0, 0), rot=0, aim=0, speed=6, turnspeed=5):
        self.id = _id
        self.pos = pos
        self.rot = rot
        self.aim = aim
        self.speed = speed
        self.turnspeed = turnspeed
        self.setup()
        
    def setup(self):
        print(os.path.join(os.getcwd(),"assets/pictures/tank_{}_bottom.png"))
        self.body = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/tank_{}_bottom.png").format(colors[self.id]))
        self.turret = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/tank_{}_top.png").format(colors[self.id]))
    
    def assignRot(self, pic, rot):
        rotated = pygame.transform.rotate(pic, rot + 270)
        rect = rotated.get_rect()
        rect.center = (self.pos.x - (rect[2] / 2),self.pos.y - (rect[2] / 2))
        return rotated, rect.center
    
    def draw(self, screen, pos=None, rot=None, aim=0):
        if pos != None:
            self.pos = pos
        if rot != None:
            self.rot = rot
        self.aim = aim
        screen.blit(*self.assignRot(self.body, self.rot))
        screen.blit(*self.assignRot(self.turret, self.rot + self.aim))
        return screen
