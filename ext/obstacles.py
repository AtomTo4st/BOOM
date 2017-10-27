import pygame
from collections import namedtuple
from _operator import pos
from ext.tank import Tank
from keyboard.keyboard import play

Position = namedtuple("Position", ["x", "y"])



class Obstacle():
    
    def __init__(self):
        sand = Sand(Position(0, 891), Position(402, 1200))
        sand2 = Sand(Position(402, 343), Position(805, 693))
        sand3 = Sand(Position(842, 115), Position(413, 1200))
        sand4 = Sand(Position(700, 0), Position(890, 155))
        sand5 = Sand(Position(1325, 0), Position(1740, 525))
        sand6 = Sand(Position(1325, 0), Position(1800, 173))
        stone = Stone(Position(209, 160), Position(402, 343))
        stone2 = Stone(Position(838, 541), Position(960, 656))
        magiccccFog = MagiccccFog(Position(1320, 750), Position(1800, 1200))
        bermuddaHole = BermuddaHole(Position(1426, 857), Position(1800, 1200))
        
        self.listObstacles = [sand, sand2,sand3,sand4,sand5,sand6, stone, stone2, bermuddaHole, magiccccFog]

    def onObstacle(self, playerPos = Position(0,0)):
        for obs in self.listObstacles:
            if playerPos.x > obs.pos.x and playerPos.x < obs.pos2.x:
                if playerPos.y > obs.pos.y and playerPos.y < obs.pos2.y:
                    return obs.type
        return ""
        
class Sand():
    
    #Why am I so slow? :/
    
    #Effect: Sand reduces the velocity of the player, for instance the tank
    
    def __init__(self, pos = Position(0,0), pos2 = Position(0,0)):
        self.pos = pos  
        self.pos2 = pos2
        self.type = "Sand"              
    
class Stone():
    
    #Boom! The player has faced a massive swatter and died instantly
    
    #Effect: Player dies (Tank explodes or smt like that)
    
    def __init__(self, pos = Position(0,0), pos2 = Position(0,0)):
        self.pos = pos
        self.pos2 = pos2
        self.type = "Stone"
    
class MagiccccFog():
    
    #Hugh?! Where am I? What is happening to meeee o.0... Ohhh no... My steering was inverted
    
    #Effect: Invert steering
    
    def __init__(self, pos = Position(0,0), pos2 = Position(0,0)):
        self.pos = pos
        self.pos2 = pos2
        self.type = "MagiccccFog"
    
class BermuddaHole():
    
    #It's so dark in here... This is the end... The player has been swallowed, he disappeared and he won't return
    
    #Effect: Tank disappeares
    
    def __init__(self, pos = Position(0,0), pos2 = Position(0,0)):
        self.pos = pos
        self.pos2 = pos2
        self.type = "BermuddaHole"
    
