#Emma Hoffman
#learn how to change colors 
#learn how to draw shapes
#learn how to control objects on screen with keys

import pygame
import time, sys, os

from pygame.constants import GL_GREEN_SIZE
os.system("clr")
pygame.init() #initialize the game
purple=[200,0,200]
white=[255,255,255]
red=[200,25,0]
green=[0,200,50]
WIDTH=500
HEIGHT=600

#create object to open window
screen=pygame.display.set_mode((WIDTH,HEIGHT))  #declaring our screen or window
screen.fill(green)
BG=pygame.image.load("Images/forest background.jpg")
Hunter=pygame.image.load("Images/hunter robot.png")
pygame.time.delay(100)
pygame.display.set_caption("Practice Game")
x=10
y=10
x1=50
y1=50
wbox=20
hbox=20
rect1=pygame.Rect(x,y,wbox,hbox)
rect2=pygame.Rect(x1,y1,wbox,hbox)
#variables to control our rect 
speed=5
jump=10
rad=30

check = True
JumpCheck=False          #all your programs MUST have this!!
while check:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check = False
    KB=pygame.key.get_pressed() #checking if a key has been pressed
    if KB[pygame.K_RIGHT]:
        rect1.x +=speed #move rectange 2 pixels to the right
    if KB[pygame.K_r]:
        rad+=speed
    if KB[pygame.K_LEFT]:
        rect1.x -= speed #move rectange 2 pixels to the right
    if KB[pygame.K_e]:
        rad-= speed
#code for jumping
    if not JumpCheck:
        if KB[pygame.K_UP]:
            rect1.y-= speed
        if KB[pygame.K_DOWN]:
            rect1.y += speed
        if KB[pygame.K_SPACE]:
            JumpCheck= True
    else:
        if jump >= -10:
            rect1.y-=(jump*abs(jump))/2
            jump -=1
        else:
            jump=10
            JumpCheck=False
    

    if KB[pygame.K_d]:
        rect2.x +=speed #move rectange 2 pixels to the right
    if KB[pygame.K_a]:
        rect2.x -= speed #move rectange 2 pixels to the right
    if KB[pygame.K_f]:
        rect2.y-= speed
    if KB[pygame.K_x]:
        rect2.y += speed
    

    if rect1.x <0: rect1.x=0
    if rect1.x>WIDTH-wbox: rect1.x=WIDTH-wbox
    if rect1.y<0: rect1.y=0
    if rect1.y>HEIGHT-hbox: rect1.y=HEIGHT-hbox

    if rect2.x <0: rect2.x=0
    if rect2.x>WIDTH-wbox: rect2.x=WIDTH-wbox
    if rect2.y<0: rect2.y=0
    if rect2.y>HEIGHT-hbox: rect2.y=HEIGHT-hbox
    if rad<0: rad =1 
    if rad>WIDTH/2: rad=250-x
    if rect1.colliderect(rect2):
        rect1.x -=20
        rect2.x +=20
    screen.fill(white)
    screen.blit(BG,(0,50))
    screen.blit(Hunter,(300,300))

 
    pygame.draw.rect(screen, red, rect1)
    pygame.draw.rect(screen,purple,rect2)
    pygame.draw.circle(screen,(white),(x+200, y+200), rad, 2)
    pygame.display.update()
    pygame.time.delay(25)
print("Goodbye")
pygame.time.delay(100)

pygame.quit()