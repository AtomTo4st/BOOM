import pygame, numpy as np
from collections import namedtuple
from _operator import pos
from tank import Tank

Position = namedtuple("Position", ["x", "y"])

class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self, pos = Position(0, 0)):
        self.pos = pos
        sand = Sand(Position(0, 0), Position(0, 0))
        sand2 = Sand(Position(0, 0), Position(0, 0))
        stone = Stone(Position(0, 0), Position(0, 0))
        stone2 = Stone(Position(0, 0), Position(0, 0))
        magiccccFog = MagiccccFog(Position(0, 0), Position(0, 0))
        bermuddaHole = BermuddaHole(Position(0, 0), Position(0, 0))
        
        self.listObstacles = [sand, sand2, stone, stone2, bermuddaHole, magiccccFog]
        
    def onObstacle(self, playerPos = Position(0,0)):
        for obs in self.listObstacles:
            if playerPos.x > obs.pos.x and playerPos.x < obs.pos2.x:
                if playerPos.y > obs.pos.y and playerPos.y < obs.pos2.y:
                    return obs.type
            return ""
        
class Sand(pygame.sprite.Sprite):
    
    #Why am I so slow? :/
    
    #Effect: Sand reduces the velocity of the player, for instance the tank
    
    def __init(self, pos = Position(0,0), pos2 = Position(0,0), type = "Sand"):
        self.pos = pos  
        self.pos2 = pos2
        self.type = type              
    
class Stone(pygame.sprite.Sprite):
    
    #Boom! The player has faced a massive swatter and died instantly
    
    #Effect: Player dies (Tank explodes or smt like that)
    
    def __init(self, pos = Position(0,0), pos2 = Position(0,0), type = "Stone"):
        self.pos = pos
        self.pos2 = pos2
        self.type = type
    
class MagiccccFog(pygame.sprite.Sprite):
    
    #Hugh?! Where am I? What is happening to meeee o.0... Ohhh no... My steering was inverted
    
    #Effect: Invert steering
    
    def __init(self, pos = Position(0,0), pos2 = Position(0,0), type = "MagiccccFog"):
        self.pos = pos
        self.pos2 = pos2
        self.type = type
    
class BermuddaHole(pygame.sprite.Sprite):
    
    #It's so dark in here... This is the end... The player has been swallowed, he disappeared and he won't return
    
    #Effect: Tank disappeares
    
    def __init(self, pos = Position(0,0), pos2 = Position(0,0), type = "BermuddaHole"):
        self.pos = pos
        self.pos2 = pos2
        self.type = type
    
