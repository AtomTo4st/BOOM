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
        self.pos = Position(int(pos.x) + 60, pos.y)
        self.rot = rot
        self.aim = aim
        self.speed = speed
        self.turnspeed = turnspeed
        self.body = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/tank_{}_bottom.png").format(colors[self.id]))
        self.turret = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/tank_{}_top.png").format(colors[self.id]))
        self.trigger = False
        self.lasttrigger = False
        self.bullets = []
        self.obstacle = 0 # 0 = keins, 1= sand, 2 = stone, 3 = fog, 4 = bermuda
        
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
        self.pos = Position(int(pos.x) + 60, pos.y)
         
        if self.trigger == True:
            print("Trigger pressed")
            self.aim = self.aim + steer/128 * self.turnspeed
            if self.aim <= 0:
                self.aim = 360 + self.aim
            elif self.aim >= 360:
                self.aim = 0 + self.aim-360
            self.lasttrigger = True
        elif self.trigger == False:
            if self.lasttrigger == True and not (self.obstacle == 2 or self.obstacle == 4):
                self.bullets.append(Bullet(self.rot+self.aim, self.pos, colors[self.id]))
                self.lasttrigger = False
        if not self.obstacle == 4:
            screen.blit(*self.assignRot(self.body, self.rot))
            screen.blit(*self.assignRot(self.turret, self.rot + self.aim))
        print(self.id,"; rot: ",self.rot,"; aim: ",self.aim)
        
        hitEnemy = False
        for b in self.bullets:
            b.fly()
            if b.hasHit(enemyPos):
                self.bullets.remove(b)
                hitEnemy = True
                print("Hit")
            elif b.isDead(screen.get_width(), screen.get_height()):
                self.bullets.remove(b)
            screen.blit(b.img, [b.pos.x -32,b.pos.y -32])

       

        return screen, hitEnemy
