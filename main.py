import pygame
import sys
import time
import math
import colors
import os


pygame.init()



screen_w = 800
screen_h = 800

rec_pos_x = screen_w / 2
rec_pos_y = screen_h / 2

rec_w = 100
rec_h = 100

rec_speed = 5
rec_rotation = 0



def new_pos (old_pos_x, old_pos_y, rotation, speed):
    new_pos_x = (speed * math.sin(math.radians(rotation))) + old_pos_x
    new_pos_y = (speed * math.cos(math.radians(rotation))) + old_pos_y
    return new_pos_x, new_pos_y
    
    
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("B00M")

img_player = pygame.image.load("C:\projects\Hackathon\workspace\Boom\player.png")
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
        rec_rotation += 5
    if k_right:
        rec_rotation -= 5
    rec_pos_x, rec_pos_y = new_pos(rec_pos_x, rec_pos_y, rec_rotation, rec_speed)
    #pygame.draw.rect(screen, colors.red, (rec_pos_x, rec_pos_y, rec_w, rec_h))
    
    rotated_img_player = pygame.transform.rotate(img_player, rec_rotation + 90)
    rect = rotated_img_player.get_rect()
    rect.center=(rec_pos_x,rec_pos_y)
    screen.blit(rotated_img_player, (rec_pos_x,rec_pos_y))
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()