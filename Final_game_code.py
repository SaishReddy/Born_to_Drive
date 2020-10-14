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
pg.display.set_caption("BORN TO DRIVE")
clock = pg.time.Clock()
car_img = pg.image.load(
    "utilities\\Black_viper.png")
pause = False
crash_sound = pg.mixer.Sound("utilities\\crash_s.wav")
pg.mixer.music.load("utilities\\bensound-allthat.wav")


def things_dodged(count):
    font = pg.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pg.draw.rect(gameDisplay, color, [int(thingx), int(thingy), int(thingw), int(thingh)])


def car(x, y):
    gameDisplay.blit(car_img, (int(x), int(y)))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pg.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width // 2), (display_height // 2))
    gameDisplay.blit(text_surf, text_rect)
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
        large_text = pg.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("A bit Racey", large_text)
        text_rect.center = ((display_width // 2), (display_height // 2))
        gameDisplay.blit(text_surf, text_rect)
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
        textRect.center = (150 + (120 // 2), 450 + (50 // 2))
        gameDisplay.blit(textSurf, textRect)
        smallText1 = pg.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Quit", smallText1)
        textRect.center = (550 + (120 // 2), 450 + (50 // 2))
        gameDisplay.blit(textSurf, textRect)
        pg.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ac, ic, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x + w >= mouse[0] >= x and y + h >= mouse[1] >= y:
        pg.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pg.draw.rect(gameDisplay, ic, (x, y, w, h))
    text_variable = pg.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(msg, text_variable)
    text_rect.center = (x + (w // 2), y + (h // 2))
    gameDisplay.blit(text_surf, text_rect)
    pg.display.update()
    clock.tick(15)


def un_paused():
    global pause
    pg.mixer.music.unpause()
    pause = False


def quit_game():
    pg.quit()
    quit()


def paused():
    global pause
    pg.mixer.music.pause()
    largeText = pg.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width // 2), (display_height // 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # gameDisplay.fill(white)

        button("Continue", 150, 450, 100, 50, green, (0, 200, 0), un_paused)
        button("Quit", 550, 450, 100, 50, red, (200, 0, 0), quit_game)

        pg.display.update()
        clock.tick(15)


def crash():
    pg.mixer.Sound.play(crash_sound)
    pg.mixer.music.stop()
    # message_display("You Crashed")
    largeText = pg.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width // 2), (display_height // 2))
    gameDisplay.blit(TextSurf, TextRect)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        button("Retry", 150, 450, 100, 50, blue, (0, 0, 200), game_loop)
        button("Quit", 550, 450, 100, 50, red, (200, 0, 0), quit_game)
    pg.display.update()
    clock.tick(15)


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
            if thing_startx < x < thing_startx + thing_width or \
                    thing_startx < x + car_width < thing_startx + thing_width:
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

# This is one complete good game...............................
