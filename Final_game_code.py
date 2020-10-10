# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:49:25 2019

@author: ksath
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:26:42 2019

@author: ksath
"""

'''import pygame
import time
import random
 
pygame.init()
 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 
car_width = 73
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
 
carImg = pygame.image.load('C:\\Users\\ksath\\Downloads\\Topdown_vehicle_sprites_pack_Unluckystudio\\Topdown_vehicle_sprites_pack\\Black_Viper.png')
#gameIcon = pygame.image.load('carIcon.png')

#pygame.display.set_icon(gameIcon)

pause = False
#crash = True
 
def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
##def message_display(text):
##    largeText = pygame.font.SysFont("comicsansms",115)
##    TextSurf, TextRect = text_objects(text, largeText)
##    TextRect.center = ((display_width/2),(display_height/2))
##    gameDisplay.blit(TextSurf, TextRect)
## 
##    pygame.display.update()
## 
##    time.sleep(2)
## 
##    game_loop()
    
    
 
def crash():
    
    
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
    

def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
 
    thingCount = 1
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(white)
 
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
 
        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
 
        if x > display_width - car_width or x < 0:
            crash()
 
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
 
        if y < thing_starty+thing_height:
            print('y crossover')
 
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
#Author' s code
'''
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 23:31:19 2019

@author: saish
"""
import pygame as pg
import time
import random

pg.init()

display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
car_width = 65

gameDisplay = pg.display.set_mode((display_width, display_height))
pg.display.set_caption("Inputing_some_value_when_a_game_is_crashed_by_boundaries")
clock = pg.time.Clock()
# carimg=pg.image.load("C:\\Users\\ksath\\Downloads\\Topdown_vehicle_sprites_pack_Unluckystudio\\Topdown_vehicle_sprites_pack\\Black_Viper.png")
carimg = pg.image.load(
    "racecar.png")
pause = False
crash_sound = pg.mixer.Sound("crash_s.wav")
pg.mixer.music.load("C:\\Users\\saish\\PycharmProjects\\GoP\\Saish\\borntodrive\\bensound-allthat.wav")
'''def times_crashed(flag):
    font=pg.font.SysFont(None,25)
    text=font.render("Crashed: "+str(flag),True,black)
    gameDisplay.blit(text,(0,25))'''


def things_dodged(count):
    font = pg.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pg.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carimg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pg.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pg.display.update()
    time.sleep(2)
    game_loop()


def game_intro():
    intro = True
    while intro:
        for event in pg.event.get():
            # print(event)
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pg.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        mouse = pg.mouse.get_pos()
        if 150 + 100 >= mouse[0] >= 150 and 450 + 50 >= mouse[1] >= 450:
            pg.draw.rect(gameDisplay, green, (150, 450, 120, 50))
            if event.type == pg.MOUSEBUTTONDOWN:
                game_loop()
        else:
            pg.draw.rect(gameDisplay, (0, 200, 0), (150, 450, 120, 50))
        # This is normal above is interactive
        # pg.draw.rect(gameDisplay,(0,200,0),(150,450,100,50))
        if 550 + 100 >= mouse[0] >= 550 and 450 + 50 >= mouse[1] >= 450:
            pg.draw.rect(gameDisplay, red, (550, 450, 120, 50))
            if event.type == pg.MOUSEBUTTONDOWN:
                pg.quit()
                quit()

        else:
            pg.draw.rect(gameDisplay, (200, 0, 0), (550, 450, 120, 50))
        smallText = pg.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("New Game", smallText)
        textRect.center = (150 + (120 / 2), 450 + (50 / 2))
        gameDisplay.blit(textSurf, textRect)
        smallText1 = pg.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Quit", smallText1)
        textRect.center = (550 + (120 / 2), 450 + (50 / 2))
        gameDisplay.blit(textSurf, textRect)
        pg.display.update()
        clock.tick(15)


'''def button(text,text_font,text_size,button_x,button_y,button_width,button_height,ac,ic,action):
    text_variable=pg.font.Font(text_font,text_size)
    textSurf,textRect=text_objects(text,text_variable)
    textRect.center=(button_x+(button_width/2),button_y+(button_height/2))
    gameDisplay.blit(textSurf,textRect)
    mouse=pg.mouse.get_pos()
    if button_x+button_width>=mouse[0]>=button_x and button_y+button_height>=mouse[1]>=button_y:
        pg.draw.rect(gameDisplay,ac,(button_x,button_y,button_width,button_height))
        for event in pg.event.get():
            if event.type==pg.MOUSEBUTTONDOWN:
                action
    else:
        pg.draw.rect(gameDisplay,ic,(button_x,button_y,button_width,button_height))
    
    
    pg.display.update()
    clock.tick(15)'''


def button(msg, x, y, w, h, ac, ic, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    # if click[0]==1 and action!=None:
    #   action()
    if x + w >= mouse[0] >= x and y + h >= mouse[1] >= y:
        pg.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pg.draw.rect(gameDisplay, ic, (x, y, w, h))
    text_variable = pg.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, text_variable)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)
    pg.display.update()
    clock.tick(15)


def unpaused():
    global pause
    pg.mixer.music.unpause()
    pause = False


def quitgame():
    pg.quit()
    quit()


'''def paused():
    largeText=pg.font.SysFont("comicsansms",115)
    TextSurf,TextRect=text_objects("Paused",largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    while rage:    
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
        #button("New game",150,450,120,55,blue,(0,0,200),game_loop)
        button("Continue",150,450,100,50,blue,(0,0,200),unpause)
        button("Quit",550,450,100,50,red,(200,0,0),quitgame)
        pg.display.update()
        clock.tick(15)
'''


def paused():
    global pause
    pg.mixer.music.pause()
    largeText = pg.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause == True:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # gameDisplay.fill(white)

        button("Continue", 150, 450, 100, 50, green, (0, 200, 0), unpaused)
        button("Quit", 550, 450, 100, 50, red, (200, 0, 0), quitgame)

        pg.display.update()
        clock.tick(15)


def crash():
    pg.mixer.Sound.play(crash_sound)
    pg.mixer.music.stop()
    # message_display("You Crashed")
    largeText = pg.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        button("Retry", 150, 450, 100, 50, blue, (0, 0, 200), game_loop)
        button("Quit", 550, 450, 100, 50, red, (200, 0, 0), quitgame)
    pg.display.update()
    clock.tick(15)

    # pg.mixer.Sound.play(crash_sound)
    # pg.mixer.sound.play("C:\\Users\\ksath\\Downloads\\s.wav")


def game_loop():
    global pause
    pg.mixer.music.play()
    car_speed = 5
    x = display_width * 0.45
    y = display_height * 0.8
    x_change = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_width = 100
    thing_height = 100
    thing_speed = 10
    dodged = 0
    # crashed=0
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -car_speed
                if event.key == pg.K_RIGHT:
                    x_change = car_speed
                if event.key == pg.K_p:
                    pause = True
                    paused()
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, (132, 145, 89))
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)
        # times_crashed(crashed)
        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.2
            thing_width += 1.2
            car_speed += 0.1
        if y < thing_starty + thing_height:
            # print('y crossover')
            # author code if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('You crashed :)')
                pass
                #       crashed+=1
                crash()
        pg.display.update()
        clock.tick(60)


game_intro()
game_loop()
pg.quit()
quit()
# NEIL GOGTE: aziz@ngit.ac.in
# This is one complete good game...............................
