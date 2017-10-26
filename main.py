import pygame, math
from ext.tank import tank
try:
    import DasSpiel as BAPI
except ImportError:
    import DasSpielSimulation as BAPI
# BAPI may stand for "Basler API" :-)


def main():
    car_list=BAPI.getWindow().carManager.getListOfCars()
    tank_list=[]
    for i in car_list:
        tank_list.append(tank(id=i,posx=car_list[i].position.x, posy=car_list[i].position.y,rot=math.degrees(car_list[i].position)))
    while True:
        for i in tank_list:
            tank_list[i].draw(car_list[i].position, car_list[i].angle)

class manager:
    def __init__(self):
        pass