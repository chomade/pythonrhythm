import sys
import pygame
import math
import os
import time
import json

pygame.init()

screenwidth = 800
screenheight = 450

white = (255, 255, 255)
black = (0, 0, 0)

events = pygame.event.get()

mouse = pygame.mouse.get_pos()

mainbuttonheight = screenheight / 7
intmainbuttonheight = int(mainbuttonheight)
mainbuttonx = screenwidth / 10
mainbuttonwidth = screenwidth - mainbuttonx * 2
bigbuttonheight = mainbuttonheight * 1.3
intbigbuttonheight = int(bigbuttonheight)
bigbuttonwidth = mainbuttonwidth * 1.15
bigbuttonx = screenwidth / 2 - bigbuttonwidth / 2
bigbuttonbasicy = mainbuttonheight * 1.5 - bigbuttonheight / 2


setting = False
setting2 = False
setting3 = False
main_screen = True
main_screen2 = False

font = pygame.font.Font("data\DNF.otf", intmainbuttonheight)
bigfont = pygame.font.Font("data\DNF.otf", intbigbuttonheight)

screen = pygame.display.set_mode((screenwidth, screenheight))

key = {
    "First": pygame.K_d,
    "Second": pygame.K_f,
    "Third": pygame.K_j,
    "Fourth": pygame.K_k
}


class Button():
    def __init__(self, name, x, y, width, height, number):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.rect = pygame.Rect(self.x, self.y, self.width, height)


main_buttons = [
    Button("play", mainbuttonx, mainbuttonheight * 1, mainbuttonwidth, mainbuttonheight, 1),
    Button("settings", mainbuttonx, mainbuttonheight * 5, mainbuttonwidth, mainbuttonheight, 5),
]

setting_buttons = [
    Button("screen setting", mainbuttonx, mainbuttonheight * 1, mainbuttonwidth, mainbuttonheight, 1),
    Button("sound setting", mainbuttonx, mainbuttonheight * 3, mainbuttonwidth, mainbuttonheight, 3),
    Button("back", mainbuttonx, mainbuttonheight * 5, mainbuttonwidth, mainbuttonheight, 5),
]


class Key():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


keys = [
    Key(100, 0, (0, 0, 0))
]

with open("data\key.json", "w") as outfile:
    json.dump(key, outfile)


def maingame():
    global main_screen
    global main_screen2
    global setting
    screen.fill(black)
    main_screen2 = False
    setting = False
    while main_screen:
        for event in pygame.event.get():
            for button in main_buttons:
                selectnum = 0
                yplace = selectnum
                bigbuttony = bigbuttonbasicy + mainbuttonheight * yplace
                pygame.draw.rect(screen, white, button.rect)
                textsurface = font.render(button.name, True, black)
                screen.blit(textsurface, (mainbuttonx, mainbuttonheight * button.number))
                firstsels = [button for button in main_buttons if button.number == 1]
                for firstsel in firstsels:
                    pygame.draw.rect(screen, white, (bigbuttonx, bigbuttony, bigbuttonwidth, bigbuttonheight))
                    bigtextsurface = bigfont.render(firstsel.name, True, black)
                    screen.blit(bigtextsurface, (bigbuttonx, bigbuttony))
                pygame.display.update()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                main_screen2 = True
                maingame2()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                main_screen2 = True
                maingame2()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                main_screen2 = True

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()


def maingame2():
    global main_screen
    global main_screen2
    global setting
    screen.fill(black)
    main_screen = False
    setting = False
    while main_screen2:
        for event in pygame.event.get():
            for button in main_buttons:
                selectnum = 4
                yplace = selectnum
                bigbuttony = bigbuttonbasicy + mainbuttonheight * yplace
                pygame.draw.rect(screen, white, button.rect)
                textsurface = font.render(button.name, True, black)
                screen.blit(textsurface, (mainbuttonx, mainbuttonheight * button.number))
                secondsels = [button for button in main_buttons if button.number == 5]
                for secondsel in secondsels:
                        pygame.draw.rect(screen, white, (bigbuttonx, bigbuttony, bigbuttonwidth, bigbuttonheight))
                        bigtextsurface = bigfont.render(secondsel.name, True, black)
                        screen.blit(bigtextsurface, (bigbuttonx, bigbuttony))
                pygame.display.update()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                main_screen = True
                maingame()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                main_screen = True
                maingame()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                setting = True
                settinggame()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()


def settinggame():
    global setting
    global setting2
    global setting3
    global main_screen
    global main_screen2
    screen.fill(black)
    main_screen = False
    main_screen2 = False
    setting2 = False
    setting3 = False
    while setting:
        for event in pygame.event.get():
            for button in setting_buttons:
                selectnum = 0
                yplace = selectnum
                bigbuttony = bigbuttonbasicy + mainbuttonheight * yplace
                pygame.draw.rect(screen, white, button.rect)
                textsurface = font.render(button.name, True, black)
                screen.blit(textsurface, (mainbuttonx, mainbuttonheight * button.number))
                firstsels = [button for button in setting_buttons if button.number == 1]
                for firstsel in firstsels:
                    pygame.draw.rect(screen, white, (bigbuttonx, bigbuttony, bigbuttonwidth, bigbuttonheight))
                    bigtextsurface = bigfont.render(firstsel.name, True, black)
                    screen.blit(bigtextsurface, (bigbuttonx, bigbuttony))
                pygame.display.update()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                setting2 = True
                settinggame2()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                setting3 = True
                settinggame3()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                main_screen2 = True
                maingame2()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()


def settinggame2():
    global setting
    global setting2
    global setting3
    global main_screen
    global main_screen2
    screen.fill(black)
    main_screen = False
    main_screen2 = False
    setting = False
    setting3 = False
    while setting2:
        for event in pygame.event.get():
            for button in setting_buttons:
                selectnum = 2
                yplace = selectnum
                bigbuttony = bigbuttonbasicy + mainbuttonheight * yplace
                pygame.draw.rect(screen, white, button.rect)
                textsurface = font.render(button.name, True, black)
                screen.blit(textsurface, (mainbuttonx, mainbuttonheight * button.number))
                secondsels = [button for button in setting_buttons if button.number == 3]
                for secondsel in secondsels:
                    pygame.draw.rect(screen, white, (bigbuttonx, bigbuttony, bigbuttonwidth, bigbuttonheight))
                    bigtextsurface = bigfont.render(secondsel.name, True, black)
                    screen.blit(bigtextsurface, (bigbuttonx, bigbuttony))
                pygame.display.update()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                setting3 = True
                settinggame3()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                setting = True
                settinggame()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                main_screen2 = True
                maingame2()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()


def settinggame3():
    global setting
    global setting2
    global setting3
    global main_screen
    global main_screen2
    screen.fill(black)
    main_screen = False
    main_screen2 = False
    setting = False
    setting2 = False
    while setting3:
        for event in pygame.event.get():
            for button in setting_buttons:
                selectnum = 4
                yplace = selectnum
                bigbuttony = bigbuttonbasicy + mainbuttonheight * yplace
                pygame.draw.rect(screen, white, button.rect)
                textsurface = font.render(button.name, True, black)
                screen.blit(textsurface, (mainbuttonx, mainbuttonheight * button.number))
                thirdsels = [button for button in setting_buttons if button.number == 5]
                for thirdsel in thirdsels:
                    pygame.draw.rect(screen, white, (bigbuttonx, bigbuttony, bigbuttonwidth, bigbuttonheight))
                    bigtextsurface = bigfont.render(thirdsel.name, True, black)
                    screen.blit(bigtextsurface, (bigbuttonx, bigbuttony))
                pygame.display.update()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                setting = True
                settinggame()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                setting2 = True
                settinggame2()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                main_screen2 = True
                maingame2()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()





















maingame()