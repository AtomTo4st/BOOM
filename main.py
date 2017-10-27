import pygame, math, keyboard, time, os
from ext.tank import Tank
from ext.colors import Colors
from moviepy.editor import VideoFileClip 
#from ext.obstacles import Obstacle

try:
    import DasSpiel as BAPI
except ImportError:
    import DasSpielSimulation as BAPI
# BAPI may stand for "Basler API" :-)

class Manager:
    
    def __init__(self):
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
    
    def menu(self):
        intro = VideoFileClip('assets/fertiges_animationen_audio/INTRO_FERTIG.mpg')
        intro.preview()
        
        pygame.init()
        menu_gif = 0
        
        background = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/background_obstacles.png"))
        self.screen.blit(background, (0,0))
        
        img_play = pygame.image.load("assets/fertiges_animationen_audio/play_button.png")
        img_shop = pygame.image.load("assets/fertiges_animationen_audio/shop_logo.png")
        
        img_play_pos = (100,300)
        img_shop_pos = (1920 - 356, 300)
        
        select = 1
        running = True
        while running:
            self.screen.fill((255,255,255))
            self.screen.blit(background, (0,0))
            
            menu_gif += 1
            if menu_gif == 32:
                menu_gif = 1
            
            if menu_gif < 10:
                menu_gif_path = "assets/fertiges_animationen_audio/menu_gif/img000" + str(menu_gif) + ".png"
            else:
                menu_gif_path = "assets/fertiges_animationen_audio/menu_gif/img00" + str(menu_gif) + ".png"
            img_menu_gif = pygame.image.load(menu_gif_path)
            
            self.screen.blit(img_menu_gif, (0,0))
            self.screen.blit(img_play, img_play_pos)
            self.screen.blit(img_shop, img_shop_pos)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        select -= 1
                        if select >= 3:
                            select = 1 
                        elif select <= 0:
                            select = 2
                    if event.key == pygame.K_RIGHT:
                        select += 1
                        if select >= 3:
                            select = 1 
                        elif select <= 0:
                            select = 2
                    if event.key == pygame.K_RETURN:
                        if select == 1:
                            self.main()
                        if select == 2:
                            os.system("start https://www.paypal.me/JonteBehring/10")
                    if event.key == pygame.K_ESCAPE:
                        running = False
                
            if select == 1:
                pygame.draw.rect(self.screen, (0,0,0), (img_play_pos[0]-10 ,img_play_pos[1] -10 ,276,276), 6)   
            elif select == 2:
                pygame.draw.rect(self.screen, (0,0,0), (img_shop_pos[0]-10 ,img_shop_pos[1] -10 ,276,276), 6)
            
            pygame.display.update()
            self.clock.tick(20)
    
    def main(self):
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
        
        #obst = Obstacle()
        background = pygame.image.load(os.path.join(os.getcwd(),"assets/pictures/background_obstacles.png"))
        self.screen.blit(background, (0,0))

        
        mainWindow = initMainWindow("Boom", self.screen_width, self.screen_height)
        font = pygame.font.SysFont("monospace", 30)
        scores = [0,0]
        running = True
        for i in range(len(self.car_list)):
            self.tank_list.append(Tank(_id=i,pos=self.car_list[i].position,rot=-self.car_list[i].angleInDegree + 90))
        while running == True:
            self.screen.fill((255,255,255))
            self.screen.blit(background, (0,0))
            
            scoreLabel = font.render(str(scores[0]), 1, (255,0,0))
            self.screen.blit(scoreLabel, (60, 2))
            scoreLabel = font.render(str(scores[1]), 1, (0,255,0))
            self.screen.blit(scoreLabel, (self.screen_width-75, 2))
            
            winner = 0
            for s in range(len(scores)):
                if scores[s] >= 3:
                    winner = s+1
                    
            if winner != 0:
                label = font.render("WINNER IS PLAYER {} ESC to continue".format(s+1), 1, (0,0,0))
                self.screen.blit(label, (self.screen_width//2, self.screen_height//2))
                pygame.display.update()
                self.clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                continue
            
            # Basic game API code
            img = BAPI.grabFromCamera()
            mainWindow.searchCars(img)
            mainWindow.wait4Asyncs()
            
            '''print("%f, %f, %f" % (BAPI.getWindow().carManager.getListOfCars()[0].position.x,
                              BAPI.getWindow().carManager.getListOfCars()[0].position.x,
                              BAPI.getWindow().carManager.getListOfCars()[0].angle))'''
            for i in range(len(self.tank_list)):
                '''if obst.onObstacle(self.car_list[i].position) == "Sand":
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
                '''
                self.steerTanks(i,self.remote.get_in_throttle(self.remote_ip + str(i)),self.remote.get_in_steer(self.remote_ip + str(i)))
                #self.steerTanks_debug(i)
                self.screen, self.hit = self.tank_list[i].draw(self.screen,self.car_list[i].position, -self.car_list[i].angleInDegree + 90, self.steer,  self.car_list[(i+1)%2].position)
                print("hit:", self.hit)
                if self.hit:
                    scores[i] = scores[i] + 1
                     
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        
            pygame.display.update()
            self.clock.tick(30)
    
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
manager.menu()
