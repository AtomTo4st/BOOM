import pygame
import sys
import time
import math
import ext.colors as colors
import os
from pygame import image
from moviepy.editor import VideoFileClip


pygame.init()


screen_w = 800
screen_h = 800

player_1_pos = (screen_w / 4, screen_h / 4)
player_2_pos = (800 - (screen_w / 4), (screen_h / 4))


player_1_speed = 6
player_2_speed = 6
player_1_rotation = 0
player_2_rotation = 0
player_1_gun_rotation = 0
player_2_gun_rotation = 0

player_1_gun_length = 25
player_2_gun_length = 25

player_1_rotation_plus = 5
player_2_rotation_plus = 5

player_1_gun_rotation_plus = 2
player_2_gun_rotation_plus = 2

player_1_shoot_list = []
player_2_shoot_list = []

player_1_shoot_speed = 10
player_2_shoot_speed = 10



def new_pos (old_pos_x, old_pos_y, rotation, speed):
    new_pos_x = (speed * math.sin(math.radians(rotation))) + old_pos_x
    new_pos_y = (speed * math.cos(math.radians(rotation))) + old_pos_y
    return int(new_pos_x), int(new_pos_y)

def show_player(img_player, player_pos, player_rotation):
    rotated_img_player = pygame.transform.rotate(img_player, player_rotation + 270)
    rect_player = rotated_img_player.get_rect()
    rect_player.center=(player_pos[0] - (rect_player[2] / 2),player_pos[1] - (rect_player[2] / 2))
    screen.blit(rotated_img_player, (player_pos[0] - (rect_player[2] / 2),player_pos[1] - (rect_player[2] / 2)))
    
def draw_shoot(list, img_shoot):
    shoot_counter = 0
    for each_shoot in list:
        each_shoot_pos = new_pos(each_shoot[0],each_shoot[1],each_shoot[2],each_shoot[3])
        screen.blit(img_shoot, (each_shoot_pos[0]-32, each_shoot_pos[1]-32))
        list[shoot_counter] = ((each_shoot_pos[0], each_shoot_pos[1], each_shoot[2], each_shoot[3]))
        
        if each_shoot_pos[0] < 0 or each_shoot_pos[0] > screen_w or each_shoot_pos[1] < 0 or each_shoot_pos[1] > screen_h:
            del list[shoot_counter]
        
        shoot_counter +=1
    return list
  
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("B00M")

clip = VideoFileClip('assets/Animationen_Daniel/test_video.mpg')
clip.preview()
screen = pygame.display.set_mode((screen_w,screen_h))

img_player_1_tank = pygame.image.load("assets/pictures/tank_red_bottom.png")
img_player_1_gun = pygame.image.load("assets/pictures/tank_red_top.png")

img_player_2_tank = pygame.image.load("assets/pictures/tank_green_bottom.png")
img_player_2_gun = pygame.image.load("assets/pictures/tank_green_top.png")

img_player_1_shoot = pygame.image.load("assets/pictures/bullet_red.png")
img_player_2_shoot = pygame.image.load("assets/pictures/bullet_green.png")

shoot_sound = pygame.mixer.music.load("assets/sfx/tank_firing.ogg")

clock = pygame.time.Clock()
fail = False


k_left = False
k_right = False
k_w = False
k_s = False
k_space = False
k_q = False





while fail == False:
    screen.fill(colors.black)
    
    player_1_pos = new_pos(player_1_pos[0], player_1_pos[1], player_1_rotation, player_1_speed)
    player_2_pos = new_pos(player_2_pos[0], player_2_pos[1], player_2_rotation, player_2_speed)
    
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
            if event.key == pygame.K_SPACE:
                k_space = True
                player_1_speed = 3
            if event.key == pygame.K_q:
                k_q = True
                player_2_speed = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                k_left = False
            if event.key == pygame.K_RIGHT:
                k_right = False
            if event.key == pygame.K_w:
                k_w = False
            if event.key == pygame.K_s:
                k_s = False
            if event.key == pygame.K_SPACE:
                k_space = False
                player_1_speed = 6
                player_1_first_shoot_pos = new_pos(player_1_pos[0], player_1_pos[1], player_1_rotation + player_1_gun_rotation, player_1_gun_length)
                player_1_shoot_list.append((player_1_first_shoot_pos[0], player_1_first_shoot_pos[1], player_1_rotation + player_1_gun_rotation, player_1_shoot_speed))
                pygame.mixer.music.play(1, 0.0)
            if event.key == pygame.K_q:
                k_q = False
                player_2_speed = 6
                player_2_first_shoot_pos = new_pos(player_2_pos[0], player_2_pos[1], player_2_rotation + player_2_gun_rotation, player_2_gun_length)
                player_2_shoot_list.append((player_2_pos[0], player_2_pos[1], player_2_rotation + player_2_gun_rotation, player_2_shoot_speed))
                pygame.mixer.music.play(1, 0.0)
            
    if k_left:
        if k_space:
            player_1_gun_rotation += player_1_gun_rotation_plus
        else:
            player_1_rotation += player_1_rotation_plus
    if k_right:
        if k_space:
            player_1_gun_rotation -= player_1_gun_rotation_plus
        else:
            player_1_rotation -= player_1_rotation_plus
    if k_w:
        if k_q:
            player_2_gun_rotation += player_2_gun_rotation_plus
        else:
            player_2_rotation += player_2_rotation_plus
    if k_s:
        if k_q:
            player_2_gun_rotation -= player_2_gun_rotation_plus
        else:
            player_2_rotation -= player_2_rotation_plus
                  
    if player_1_rotation >= 360:
        player_1_rotation = 0
    if player_2_rotation >= 360:
        player_2_rotation = 0
        
    #pygame.draw.circle(screen, colors.red, player_2_pos, 50, )
    show_player(img_player_1_tank, player_1_pos, player_1_rotation)
    show_player(img_player_2_tank, player_2_pos, player_2_rotation)
    
    player_1_shoot_list = draw_shoot(player_1_shoot_list, img_player_1_shoot)
    player_2_shoot_list = draw_shoot(player_2_shoot_list, img_player_2_shoot)
    
    show_player(img_player_1_gun, player_1_pos, player_1_rotation + player_1_gun_rotation)
    show_player(img_player_2_gun, player_2_pos, player_2_rotation + player_2_gun_rotation)
    
    
    '''
    rotated_img_player_1_tank = pygame.transform.rotate(img_player_1_tank, player_1_rotation + 270)
    rect_player_1_tank = rotated_img_player_1_tank.get_rect()
    rect_player_1_tank.center=(player_1_pos[0] - (rect_player_1_tank[2] / 2),player_1_pos[1] - (rect_player_1_tank[2] / 2))
    screen.blit(rotated_img_player_1_tank, (player_1_pos[0] - (rect_player_1_tank[2] / 2),player_1_pos[1] - (rect_player_1_tank[2] / 2)))
    
    pygame.draw.circle(screen, colors.green, player_1_pos, 5, 0)
    '''
    
    
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()