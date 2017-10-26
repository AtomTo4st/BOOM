import pygame
import sys
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
        self.body = pygame.image.load("/assets/pictures/tank_{}_bottom.png".format(colors[self.id]))
        self.turret = pygame.image.load("/assets/pictures/tank_{}_top.png".format(colors[self.id]))
    
    def assignRot(self, pic, rot):
        rotated = pygame.transform.rotate(pic, rot + 270)
        rect = rotated.get_rect()
        rect.center = (self.pos.x - (rect[2] / 2),self.pos.y - (rect[2] / 2))
        return rotated, rect.center
    
    def draw(self, screen, pos=self.pos, rot=self.rot, aim=0):
        self.pos = pos
        self.rot = rot
        self.aim = aim
        screen.blit(self.assignRot(self.body, self.rot))
        screen.blit(self.assignRot(self.turret, self.rot + self.aim))
        return screen
