import pygame
import sys
import time
import math
import colors
import os


pygame.init()


screen_w = 800
screen_h = 800

player_1_pos = (screen_w / 4, screen_h / 4)


player_1_speed = 5
player_2_speed = 5
player_1_rotation = 0
player_2_rotation = 0



def new_pos (old_pos_x, old_pos_y, rotation, speed):
    new_pos_x = (speed * math.sin(math.radians(rotation))) + old_pos_x
    new_pos_y = (speed * math.cos(math.radians(rotation))) + old_pos_y
    return new_pos_x, new_pos_y
    
    
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("B00M")

img_player_1_tank = pygame.image.load("assets\pictures\car.png")
#img_player_1_gun = pygame.image.load("")

#img_player_2_tank = pygame.image.load()
#img_player_2_gun = pygame.image.load()


clock = pygame.time.Clock()
fail = False

right_pressed = False
left_pressed = False

k_left = False
k_right = False

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                k_left = False
            if event.key == pygame.K_RIGHT:
                k_right = False
            
    if k_left:
        player_1_rotation += 5
    if k_right:
        player_1_rotation -= 5
    player_1_pos = new_pos(player_1_pos[0], player_1_pos[1], player_1_rotation, player_1_speed)
    
    rotated_img_player_1_tank = pygame.transform.rotate(img_player_1_tank, player_1_rotation + 270)
    rect_player_1_tank = rotated_img_player_1_tank.get_rect()
    rect_player_1_tank.center=(player_1_pos[0],player_1_pos[1])
    screen.blit(rotated_img_player_1_tank, player_1_pos)
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()