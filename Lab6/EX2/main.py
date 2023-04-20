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
firstObject = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
while(run):
    screen.fill((255, 255, 255))
    firstObject.c = (65,105,225)
    firstObject.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            firstObject.x += 100     
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            firstObject.x -= 100
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            firstObject.y += 100
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            firstObject.y -= 100
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
