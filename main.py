import pygame
import sys
import time
import math
import colors
import os
from pygame import image


pygame.init()


screen_w = 800
screen_h = 800

player_1_pos = (screen_w / 4, screen_h / 4)
player_2_pos = (800 - (screen_w / 4), 800 - (screen_h / 4))


player_1_speed = 5
player_2_speed = 5
player_1_rotation = 0
player_2_rotation = 0

player_1_rotation_plus = 5
player_2_rotation_plus = 5



def new_pos (old_pos_x, old_pos_y, rotation, speed):
    new_pos_x = (speed * math.sin(math.radians(rotation))) + old_pos_x
    new_pos_y = (speed * math.cos(math.radians(rotation))) + old_pos_y
    return int(new_pos_x), int(new_pos_y)

def show_player(img_player, player_pos, player_rotation):
    rotated_img_player = pygame.transform.rotate(img_player, player_rotation + 270)
    rect_player = rotated_img_player.get_rect()
    rect_player.center=(player_pos[0] - (rect_player[2] / 2),player_pos[1] - (rect_player[2] / 2))
    screen.blit(rotated_img_player, (player_pos[0] - (rect_player[2] / 2),player_pos[1] - (rect_player[2] / 2)))
  
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("B00M")

img_player_1_tank = pygame.image.load("assets/pictures/tank_red_bottom.png")
img_player_1_gun = pygame.image.load("assets/pictures/tank_red_top.png")

img_player_2_tank = pygame.image.load("assets/pictures/tank_green_bottom.png")
img_player_2_gun = pygame.image.load("assets/pictures/tank_green_top.png")


clock = pygame.time.Clock()
fail = False


k_left = False
k_right = False
k_w = False
k_s = False


while fail == False:
    screen.fill(colors.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fail = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                k_left = True
            if event.key == pygame.K_RIGHT:
                k_right = True
            if event.key == pygame.K_w:
                k_w = True
            if event.key == pygame.K_s:
                k_s = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                k_left = False
            if event.key == pygame.K_RIGHT:
                k_right = False
            if event.key == pygame.K_w:
                k_w = False
            if event.key == pygame.K_s:
                k_s = False
            
    if k_left:
        player_1_rotation += player_1_rotation_plus
    if k_right:
        player_1_rotation -= player_1_rotation_plus
    if k_w:
        player_2_rotation += player_2_rotation_plus
    if k_s:
        player_2_rotation -= player_2_rotation_plus
        
    if player_1_rotation >= 360:
        player_1_rotation = 1
    if player_2_rotation >= 360:
        player_2_rotation = 1    
    player_1_pos = new_pos(player_1_pos[0], player_1_pos[1], player_1_rotation, player_1_speed)
    player_2_pos = new_pos(player_2_pos[0], player_2_pos[1], player_2_rotation, player_2_speed)
    #pygame.draw.circle(screen, colors.red, player_2_pos, 50, )
    show_player(img_player_1_tank, player_1_pos, player_1_rotation)
    show_player(img_player_2_tank, player_2_pos, player_2_rotation)
    show_player(img_player_1_gun, player_1_pos, player_1_rotation)
    show_player(img_player_2_gun, player_2_pos, player_2_rotation)
    show_player(img_player_1_gun, player_1_pos, -player_1_rotation)
    show_player(img_player_2_gun, player_2_pos, -player_2_rotation)
    
    '''
    rotated_img_player_1_tank = pygame.transform.rotate(img_player_1_tank, player_1_rotation + 270)
    rect_player_1_tank = rotated_img_player_1_tank.get_rect()
    rect_player_1_tank.center=(player_1_pos[0] - (rect_player_1_tank[2] / 2),player_1_pos[1] - (rect_player_1_tank[2] / 2))
    screen.blit(rotated_img_player_1_tank, (player_1_pos[0] - (rect_player_1_tank[2] / 2),player_1_pos[1] - (rect_player_1_tank[2] / 2)))
    
    rotated_img_player_1_gun = pygame.transform.rotate(img_player_1_gun, player_1_rotation + 270)
    rect_player_1_gun = rotated_img_player_1_gun.get_rect()
    rect_player_1_gun.center=(player_1_pos[0] - (rect_player_1_gun[2] / 2),player_1_pos[1] - (rect_player_1_gun[2] / 2))
    screen.blit(rotated_img_player_1_gun, (player_1_pos[0] - (rect_player_1_gun[2] / 2),player_1_pos[1] - (rect_player_1_gun[2] / 2)))
    
    rotated_img_player_2_tank = pygame.transform.rotate(img_player_2_tank, player_2_rotation + 270)
    rect_player_2_tank = rotated_img_player_2_tank.get_rect()
    rect_player_2_tank.center=(player_2_pos[0],player_2_pos[1])
    screen.blit(rotated_img_player_2_tank, player_2_pos)
    
    print(rect_player_1_tank[2])
    
    rotated_img_player_2_gun = pygame.transform.rotate(img_player_2_gun, player_2_rotation + 270)
    rect_player_2_gun = rotated_img_player_2_gun.get_rect()
    rect_player_2_gun.center=(player_2_pos[0],player_2_pos[1])
    screen.blit(rotated_img_player_2_gun, player_2_pos)
    '''
    #pygame.draw.circle(screen, colors.green, player_1_pos, 5, 0)
    
    
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()