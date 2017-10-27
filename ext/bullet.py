import pygame, math, os
from collections import namedtuple
import sys
sys.path.append("../")

Position = namedtuple("Position", ["x","y"])

class Bullet:
    def __init__(self, direction=0, pos=Position(0,0), color="grey", hitradius=30, speed=15):
        self.direction = direction
        self.pos = Position( pos.x + int(30 * math.sin(math.radians(self.direction)))
                             ,pos.y + int(30 * math.cos(math.radians(self.direction))))
        self.speed = speed
        self.color = color
        self.hitRadius = hitradius
        self.img = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/bullet_{}.png").format(self.color))
        
    def isDead(self, maxW, maxH):
        if self.pos.x < 0 or self.pos.x > maxW or self.pos.y < 0 or self.pos.y > maxH:
            return True
        else:
            return False
    
    def hasHit(self, enemyPos):
        if math.sqrt(((abs(self.pos.x-enemyPos.x))**2)+((abs(self.pos.y-enemyPos.y))**2)) <= self.hitRadius:
            return True
        else:
            return False
    def fly(self):
        self.pos = Position( self.pos.x + int(self.speed * math.sin(math.radians(self.direction)))
                             ,self.pos.y + int(self.speed * math.cos(math.radians(self.direction))))
