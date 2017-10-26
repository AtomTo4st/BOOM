import pygame, math, colors
from ext.tank import tank
try:
    import DasSpiel as BAPI
except ImportError:
    import DasSpielSimulation as BAPI
# BAPI may stand for "Basler API" :-)

class Manager:
    
    def __init__(self):
        self.running = True
        self.screen_width = 800
        self.screen_height = 800    
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("B00M")
        self.clock = pygame.time.Clock()
    
    def main(self):
        pygame.init()
        car_list=BAPI.getWindow().carManager.getListOfCars()
        tank_list=[]
        for i in range(len(car_list)):
            print(car_list[i].angle)
            tank_list.append(tank(_id=i,posx=math.degrees(car_list[i].position.x), posy=car_list[i].position.y,rot=math.degrees(car_list[i].position.x)))
        while self.running == True:
            self.screen.fill(colors.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            for i in range(len(tank_list)):
                    tank_list[i].draw(car_list[i].position, car_list[i].angle)
            pygame.display.update()
            self.clock.tick(30)
        
        pygame.quit()
        
manager = Manager()
manager.main()