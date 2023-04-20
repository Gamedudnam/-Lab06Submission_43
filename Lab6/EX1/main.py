class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.c = (r,g,b) # color
    def draw(self,screen):
        pg.draw.rect(screen,(self.c),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, c=0):
        Rectangle.__init__(self, x, y, w, h, c)
    
    def isMouseOn(self):
        if self.x <= pg.mouse.get_pos()[0] <= self.x + self.w and self.y <= pg.mouse.get_pos()[1] <= self.y + self.h:
            return True
        else:
            return False
    def isMousekang(self):
        if self.x <= pg.mouse.get_pos()[0] <= self.x + self.w and self.y <= pg.mouse.get_pos()[1] <= self.y + self.h and pg.mouse. get_pressed()[0] == True:
            return True

import sys 
import pygame as pg
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    btn.c = (250,0,0)
    if btn.isMouseOn():
        btn.c = (192,192,192)
    if btn.isMousekang():
        btn.c = (128,0,128)
    btn.draw(screen)

    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False







