import pygame
from collections import namedtuple
#sys.path.append("../")

Position = namedtuple("Position", ["x","y"])

class Bullet:
    def __init__(self, direction=0, pos=Position(0,0), color="grey", hitradius=25, speed=10):
        self.direction = direction
        pos.x += int(30 * math.sin(math.radians(self.direction)))
        pos.y += int(30 * math.sin(math.radians(self.direction)))
        self.pos = pos
        self.speed = speed
        self.color = color
        self.hitradius = hitradius
        self.img = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/bullet_{}.png").format(self.color))
        
    def isDead(self, maxW, maxH, enemyPos):
        if self.pos.x < 0 or self.pos.x > maxW or self.pos.y < 0 or self.pos.y > maxH:
            return True
        elif math.sqrt(((abs(self.pos.x-enemyPos.x))**2)+((abs(self.pos.y-enemyPos.y))**2)) <= self.hitRadius:
            return True
        else:
            return False
    
    def fly(self):
        self.pos.x += int(self.speed * math.sin(math.radians(self.direction)))
        self.pos.y += int(self.speed * math.cos(math.radians(self.direction)))