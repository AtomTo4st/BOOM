import pygame, math, keyboard, time, os
from ext.tank import Tank
from ext.colors import Colors
from ext.obstacles import Obstacle
try:
    import DasSpiel as BAPI
except ImportError:
    import DasSpielSimulation as BAPI
# BAPI may stand for "Basler API" :-)

class Manager:
    
    def __init__(self):
        self.running = True
        self.screen_width = 1920
        self.screen_height = 1200    
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("B00M")
        self.clock = pygame.time.Clock()
        self.car_list = BAPI.getWindow().carManager.getListOfCars()
        self.remote = BAPI.getWindow().getCommTransmitter()
        self.tank_list = []
        self.remote_ip="192.168.0.10"
        self.offset = 128
        self.minThrottle = 5
        self.minThrottle_live = 28
        self.maxThrottle = 10
        self.maxThrottle_live = 35
        self.steer = 0
        self.hit = False
    
    def main(self):
        pygame.init()
        mainWindow = initMainWindow("Boom", self.screen_width, self.screen_height)
        background = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/background_obstacles.png"))
        self.screen.blit(background, (0,0))
        obst = Obstacle()
        
        for i in range(len(self.car_list)):
            self.tank_list.append(Tank(_id=i,pos=self.car_list[i].position,rot=-self.car_list[i].angleInDegree + 90))
        
        while self.running == True:
            self.screen.fill((255,255,255))
            self.screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Basic game API code
            img = BAPI.grabFromCamera()
            mainWindow.searchCars(img)
            mainWindow.wait4Asyncs()
            
            '''#print("%f, %f, %f" % (BAPI.getWindow().carManager.getListOfCars()[0].position.x,
                              BAPI.getWindow().carManager.getListOfCars()[0].position.x,
                              BAPI.getWindow().carManager.getListOfCars()[0].angle))'''
            for i in range(len(self.tank_list)):
                if obst.onObstacle(self.car_list[i].position) == "Sand":
                    # geschwindigkeit reduzieren
                    self.tank_list[i].obstacle = 1
                    print("SAAAAAND")
                elif obst.onObstacle(self.car_list[i].position) == "Stone":
                    #zuende
                    self.tank_list[i].obstacle = 2
                elif obst.onObstacle(self.car_list[i].position) == "MagiccccFog":
                    #invertiert lenkung
                    self.tank_list[i].obstacle = 3
                elif obst.onObstacle(self.car_list[i].position) == "BermuddaHole":
                    #unsichtbar, kann nicht schiessen
                    self.tank_list[i].obstacle = 4
                else:
                     self.tank_list[i].obstacle = 0
                #self.steerTanks(i,self.remote.get_in_throttle(self.remote_ip + str(i)),self.remote.get_in_steer(self.remote_ip + str(i)))
                self.steerTanks_debug(i)

                #self.screen, self.hit = self.tank_list[i].draw(self.screen,Position(self.car_list[i].position.x + 60, self.car_list[i].position.y), -self.car_list[i].angleInDegree + 90, self.steer,  self.car_list[(i+1)%2].position)
                self.screen, self.hit = self.tank_list[i].draw(self.screen,self.car_list[i].position, -self.car_list[i].angleInDegree + 90, self.steer,  self.car_list[(i+1)%2].position)
                #print("hit:", self.hit)
                if self.hit:
                    pygame.quit()
                
                     

            pygame.display.update()
            self.clock.tick(30)
        
        pygame.quit()
    
    def steerTanks(self, id, throttle, steering):
        if not self.hit:
            if throttle > 200 :
                #feuermodus
                self.car_list[id].throttle = self.minThrottle_live
                self.tank_list[id].trigger = True
                self.car_list[id].steeringAngle = 0
            else:
                self.tank_list[id].trigger = False 
                if  self.tank_list[id].obstacle == 1:
                    self.car_list[id].throttle = self.maxThrottle_live - 5
                elif  self.tank_list[id].obstacle == 2:
                    self.car_list[id].throttle = 0
                else:
                    self.car_list[id].throttle = self.maxThrottle_live 
                self.car_list[id].steeringAngle = steering - self.offset
            self.steer = steering - self.offset
        else:
            self.steer = 0
            self.car_list[id].throttle = 0
            self.car_list[id].steeringAngle = 0

        if self.tank_list[id].obstacle == 3:
            self.car_list[id].steeringAngle*=-1
        steer_override = limitToUInt8(self.car_list[id].steeringAngle + self.offset)
        throttle_override = limitToUInt8(self.car_list[id].throttle + self.offset)
        self.remote.set_override_out_both(self.remote_ip+str(id), steer_override, throttle_override)
           
    def steerTanks_debug(self, id):
        if keyboard.is_pressed("f"):
            throttle=201
        else :
            throttle = 0
        if keyboard.is_pressed("a"):
            steer = 28
        elif keyboard.is_pressed("d"):
            steer = 228
        else:
            steer = 128
        self.steerTanks(id, throttle, steer)
        '''if not self.hit:
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
                    self.car_list[1].steeringAngle = -100
                    self.steer = -100
                elif keyboard.is_pressed("d"):
                    self.car_list[1].steeringAngle = 100
                    self.steer = 100
                else:
                    self.car_list[1].steeringAngle = 0
                    self.steer = 0
        else:
            self.car_list[id].throttle = 0
            self.car_list[id].steeringAngle = 0
            self.steer = 0'''
            

def initMainWindow(name, fieldWidthPx, fieldHeightPx):
    mainWindow = BAPI.getWindow()
    mainWindow.setSize(fieldWidthPx, fieldHeightPx)
    mainWindow.name = name
    mainWindow.showFPS = True
    #BAPI.closeWindow(name)
    return mainWindow

def limitToUInt8(value):
    if value > 255:
        return 255
    elif value < 0:
        return 0
    else:
        return value;
       

        
manager = Manager()
manager.main()
