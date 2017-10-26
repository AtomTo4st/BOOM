import pygame
import sys, os
from collections import namedtuple
from ext.bullet import Bullet
sys.path.append("../")

colors = ["red", "green", "blue", "white"]
Position = namedtuple("Position", ["x","y"])

class Tank:
    def __init__(self, _id=0, pos=Position(100, 100), rot=0, aim=0, speed=6, turnspeed=5):
        self.id = _id
        self.pos = pos
        self.rot = rot
        self.aim = aim
        self.speed = speed
        self.turnspeed = turnspeed
        self.body = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/tank_{}_bottom.png").format(colors[self.id]))
        self.turret = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/tank_{}_top.png").format(colors[self.id]))
        self.trigger = False
        self.lasttrigger = False
        self.bullets = []
        
    def assignRot(self, pic, rot):
        rotated = pygame.transform.rotate(pic, rot + 270)
        rect = rotated.get_rect()
        rect.center = (self.pos.x - (rect[2] / 2), self.pos.y - (rect[2] / 2))
        return rotated, rect.center
    
    def draw(self, screen, pos=None, rot=None, steer=0, enemyPos=Position(0,0)):
        if pos != None:
            self.pos = pos
        if rot != None:
            self.rot = rot
        
        screen.blit(*self.assignRot(self.body, self.rot))
        screen.blit(*self.assignRot(self.turret, self.rot + self.aim))
        
        if self.trigger == True:
            self.aim = self.aim + steer/128 * turnspeed
            self.lasttrigger = True
        elif self.trigger == False:
            if self.lasttrigger == True:
                self.bullets.append(Bullet(self.rot+self.aim, self.pos, self.color))
                self.lasttrigger = False
        
        for b in range(len(self.bullets)):
            self.bullets[b].fly()
            if self.bullets[b].hasHit(enemyPos):
                self.bullets.remove(b)
                print("Hit")
            elif self.bullets[b].isDead(1800, 1200):
                self.bullets.remove(b)
            screen.blit(b.img, b.pos)
        
        return screen
