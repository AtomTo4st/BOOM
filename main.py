import pygame, math 
from ext.tank import Tank
from ext.colors import Colors
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
            tank_list.append(Tank(_id=i,pos=car_list[i].position,rot=math.degrees(car_list[i].angle)))
        while self.running == True:
            self.screen.fill(Colors.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            for i in range(len(tank_list)):
                    self.screen = tank_list[i].draw(self.screen,car_list[i].position, car_list[i].angle)
            pygame.display.update()
            self.clock.tick(30)
        
        pygame.quit()
        
manager = Manager()
manager.main()
