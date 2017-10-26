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
        self.screen_width = 1300
        self.screen_height = 700    
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("B00M")
        self.clock = pygame.time.Clock()
        self.car_list = BAPI.getWindow().carManager.getListOfCars()
        self.remote = BAPI.getWindow().getCommTransmitter()
        self.tank_list = []
        self.remote_ip="192.168.0.10"
        self.offset = 128
        self.minThrottle = 12
        self.minThrottle = 40
    
    def main(self):
        pygame.init()
        mainWindow = initMainWindow("Boom", self.screen_width, self.screen_height)
        
        for i in range(len(self.car_list)):
            self.tank_list.append(Tank(_id=i,pos=self.car_list[i].position,rot=-self.car_list[i].angleInDegree + 90))
        
        while self.running == True:
            self.screen.fill(Colors.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Basic game API code
            img = BAPI.grabFromCamera()
            mainWindow.searchCars(img)
            mainWindow.wait4Asyncs()
            
            print("%f, %f, %f" % (BAPI.getWindow().carManager.getListOfCars()[0].position.x,
                              BAPI.getWindow().carManager.getListOfCars()[0].position.x,
                              BAPI.getWindow().carManager.getListOfCars()[0].angle))
            for i in range(len(self.tank_list)):
                self.screen = self.tank_list[i].draw(self.screen,self.car_list[i].position, -self.car_list[i].angleInDegree + 90, self.car_list[(i+1)%2].position)
                self.steerTanks(i,self.remote.get_in_throttle(self.remote_ip + str(i)),self.remote.get_in_steer(self.remote_ip + str(i)))
            pygame.display.update()
            self.clock.tick(30)
        
        pygame.quit()
    
    def steerTanks(self, id, throttle, steering):
        
        if throttle < self.offset:
            #feuermodus
            self.car_list[id].throttle = self.minThrottle 
        else:
            self.car_list[id].throttle = self.maxThrottle 
            self.car_list[id].steering = steering

def initMainWindow(name, fieldWidthPx, fieldHeightPx):
    mainWindow = BAPI.getWindow()
    mainWindow.setSize(fieldWidthPx, fieldHeightPx)
    mainWindow.name = name
    mainWindow.showFPS = True
    #BAPI.closeWindow(name)
    return mainWindow

        
manager = Manager()
manager.main()
