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
        else:
            return False

#Final
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isdigit() == False:
                        self.text += event.unicode
                    else:
                        self.text += ''
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class checknumber:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text += ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else :
                    if event.unicode.isdigit():
                        self.text += event.unicode
                    else:
                        self.text += ''
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))


COLOR_INACTIVE = pg.Color('#DC143C') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 70, 100, 50) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 100, 50) # สร้าง InputBox2
input_box3 = checknumber(100, 350 ,100 ,50)
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

font = pg.font.Font('freesansbold.ttf', 25) # font and fontsize
text = font.render('First name', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (195, 40)

font1 = pg.font.Font('freesansbold.ttf', 25) # font and fontsize
text1 = font1.render('Last name', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect1 = text1.get_rect() # text size
textRect1.center = (195, 170)

font2 = pg.font.Font('freesansbold.ttf', 25) # font and fontsize
text2 = font2.render('Age', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (195, 320)

font4 = pg.font.Font('freesansbold.ttf', 35) # font and fontsize
text4 = font4.render('Submit', True, (245,189,31)) # (text,is smooth?,letter color,background color)
textRect4 = text4.get_rect() # text size
textRect4.center = (645, 370)

# font5 = pg.font.Font('freesansbold.ttf', 35) # font and fontsize
# text5 = font5.render('fill in please', True, (0,0,0)) # (text,is smooth?,letter color,background color)
# textRect5 = text5.get_rect() # text size
# textRect5.center = (645, 370)
 
# # create a surface object, image is drawn on it.
# imp = pg.image.load("C:\\Users\\USER\\Downloads\\qqq.jpg").convert()
 
# # Using blit to copy content from one surface to other

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(550,330,200,70)

while run:
    screen.fill((173,216,230))
    # screen.blit(imp, (400, 0))
    btn.c = (0,0,255)
    if btn.isMousekang():
        btn.c = (250,0,0)
        font3 = pg.font.Font('freesansbold.ttf', 25) # font and fontsize
        text3 = font3.render('Hello'+' '+ str(input_box1.text)+ '  ' + str(input_box2.text)+ '!' + ' ' + ",You are" + ' ' + str(input_box3.text)+ ' ' + "years old.", True, (0,145,122)) # (text,is smooth?,letter color,background color)
        textRect3 = text3.get_rect() # text size
        textRect3.center = (350, 450)
        screen.blit(text3, textRect3)
    if btn.isMousekang()==False:
        font5 = pg.font.Font('freesansbold.ttf', 35) # font and fontsize
        text5 = font5.render('Fill in please', True, (255,20,147)) # (text,is smooth?,letter color,background color)
        textRect5 = text5.get_rect() # text size
        textRect5.center = (600, 80)
        screen.blit(text5, textRect5)
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    btn.draw(screen)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text4, textRect4)
    
    print(pg.mouse.get_pos())

    pg.time.delay(1)
    pg.display.update()

