import pygame, math, keyboard
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
        self.minThrottle = 5
        self.maxThrottle = 10
        self.steer = 0
    
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
            
            '''print("%f, %f, %f" % (BAPI.getWindow().carManager.getListOfCars()[0].position.x,
                              BAPI.getWindow().carManager.getListOfCars()[0].position.x,
                              BAPI.getWindow().carManager.getListOfCars()[0].angle))'''
            for i in range(len(self.tank_list)):
                #self.steerTanks(i,self.remote.get_in_throttle(self.remote_ip + str(i)),self.remote.get_in_steer(self.remote_ip + str(i)))
                self.steerTanks_debug(i)
                self.screen = self.tank_list[i].draw(self.screen,self.car_list[i].position, -self.car_list[i].angleInDegree + 90, self.steer,  self.car_list[(i+1)%2].position)
            pygame.display.update()
            self.clock.tick(30)
        
        pygame.quit()
    
    def steerTanks(self, id, throttle, steering):
        
        if throttle < self.offset:
            #feuermodus
            self.car_list[id].throttle = self.minThrottle
            self.tank_list[id].trigger = True
            self.car_list[id].steeringAngle = 0
        else:
            self.tank_list[id].trigger = False 
            self.car_list[id].throttle = self.maxThrottle 
            self.car_list[id].steeringAngle = steering
        self.steer = steering
 
    def steerTanks_debug(self, id):
        if keyboard.is_pressed("f"):
            self.car_list[id].throttle = self.minThrottle
            self.car_list[id].steeringAngle = 0
            self.tank_list[id].trigger = True
            if keyboard.is_pressed("a"):
                self.steer = -100
            elif keyboard.is_pressed("d"):
                self.steer = 100
            else:
                self.steer=0
        else:
            self.tank_list[id].trigger = False 
            self.car_list[id].throttle = self.maxThrottle 
            if keyboard.is_pressed("a"):
                self.car_list[id].steeringAngle = -100
                self.steer = -100
            elif keyboard.is_pressed("d"):
                self.car_list[id].steeringAngle = 100
                self.steer = 100
            else:
                self.car_list[id].steeringAngle = 0
                self.steer = 0
            

def initMainWindow(name, fieldWidthPx, fieldHeightPx):
    mainWindow = BAPI.getWindow()
    mainWindow.setSize(fieldWidthPx, fieldHeightPx)
    mainWindow.name = name
    mainWindow.showFPS = True
    #BAPI.closeWindow(name)
    return mainWindow

        
manager = Manager()
manager.main()
