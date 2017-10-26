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
        self.car_list = BAPI.getWindow().carManager.getListOfCars()
        self.remote = BAPI.getWindow().getCommTransmitter()
        self.tank_list = []
        self.remote_ip="192.168.0.10"
        self.offset = 128
        self.minThrottle = 28
    
    def main(self):
        pygame.init()
        mainWindow = initMainWindow("Boom", Cfg.MAIN_WINDOW_WIDTH_PX, Cfg.MAIN_WINDOW_HEIGHT_PX)
        for i in range(len(self.car_list)):
            self.tank_list.append(Tank(_id=i,pos=self.car_list[i].position,rot=math.degrees(self.car_list[i].angle)))
        
        while self.running == True:
            self.screen.fill(Colors.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Basic game API code
            mainWindow.asyncCalcViews()
            mainWindow.wait4Asyncs()
            mainWindow.calcFront()
            mainWindow.display()
            
            
            for i in range(len(self.tank_list)):
                    self.screen = self.tank_list[i].draw(self.screen,self.car_list[i].position, self.car_list[i].angle)
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
    mainWindow.showFPS = False
    mainWindow.closeWindow()
    return mainWindow

        
manager = Manager()
manager.main()
