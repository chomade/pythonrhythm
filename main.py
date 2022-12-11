import sys
import pygame
import math
import os
import time
import json

pygame.init()

screenwidth = 960
screenheight = 540

white = (255, 255, 255)
black = (0, 0, 0)

events = pygame.event.get()

displaynumber = 0
displaysize = pygame.display.list_modes()[int(displaynumber)]

mouse = pygame.mouse.get_pos()
pygame.mouse.set_visible(False)
mainbuttonheight = screenheight / 7
mainfontsize = int(mainbuttonheight * 0.9)
mainbuttonx = screenwidth / 10
mainbuttonwidth = screenwidth - mainbuttonx * 2
bigbuttonheight = mainbuttonheight * 1.3
bigfontsize = int(bigbuttonheight * 0.9)
bigbuttonwidth = mainbuttonwidth * 1.15
bigbuttonx = screenwidth / 2 - bigbuttonwidth / 2
bigbuttonbasicy = mainbuttonheight * 1.5 - bigbuttonheight / 2


setting = False
setting2 = False
setting3 = False
main_screen = True
main_screen2 = False
screensetting = False

font = pygame.font.Font("data\DNF.otf", mainfontsize)
bigfont = pygame.font.Font("data\DNF.otf", bigfontsize)

screen = pygame.display.set_mode((screenwidth, screenheight))

key = {
    "First": pygame.K_d,
    "Second": pygame.K_f,
    "Third": pygame.K_j,
    "Fourth": pygame.K_k
}




class Key():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

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

screen_buttons = [
    Button('displaysize', mainbuttonx, mainbuttonheight * 1, mainbuttonwidth, mainbuttonheight, 1),
    Button("full screen", mainbuttonx, mainbuttonheight * 3, mainbuttonwidth, mainbuttonheight, 3),
    Button("back", mainbuttonx, mainbuttonheight * 5, mainbuttonwidth, mainbuttonheight, 5),
]

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
    global screensetting
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
                screensetting = True
                screengame()

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
                main_screen = True
                maingame()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()


def screengame():
    global setting
    global screensetting
    global displaysize
    global displaynumber
    global screenheight
    global screenwidth
    global mainbuttonheight
    global mainfontsize
    global mainbuttonx
    global mainbuttonwidth
    global bigbuttonheight
    global bigfontsize
    global bigbuttonwidth
    global bigbuttonx
    global bigbuttonbasicy
    screen.fill(black)
    setting = False
    enter = False
    displaysize = pygame.display.list_modes()
    displaylenth = len(displaysize) - 1
    while screensetting:
        for event in pygame.event.get():
            for button in setting_buttons:
                displaysize = str(pygame.display.list_modes()[displaynumber])
                selectnum = 0
                yplace = selectnum
                bigbuttony = bigbuttonbasicy + mainbuttonheight * yplace
                pygame.draw.rect(screen, white, button.rect)
                textsurface = font.render(button.name, True, black)
                screen.blit(textsurface, (mainbuttonx, mainbuttonheight * button.number))
                firstsels = [button for button in setting_buttons if button.number == 1]
                for firstsel in firstsels:
                    pygame.draw.rect(screen, white, (bigbuttonx, bigbuttony, bigbuttonwidth, bigbuttonheight))
                    bigtextsurface = bigfont.render(displaysize, True, black)
                    screen.blit(bigtextsurface, (bigbuttonx, bigbuttony))
                pygame.display.update()
                print(displaylenth)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                setting2 = True
                settinggame2()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                setting3 = True
                settinggame3()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                enter = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if displaynumber > 0:
                    displaynumber = displaynumber - 1
                    displaysize = str(pygame.display.list_modes()[displaynumber])
                    for firstsel in firstsels:
                        pygame.draw.rect(screen, white, (bigbuttonx, bigbuttony, bigbuttonwidth, bigbuttonheight))
                        bigtextsurface = bigfont.render(displaysize, True, black)
                        screen.blit(bigtextsurface, (bigbuttonx, bigbuttony))
                        pygame.display.update()
                        screenwidth = pygame.display.list_modes()[displaynumber][0]
                        screenheight = pygame.display.list_modes()[displaynumber][1]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if displaynumber < displaylenth:
                    displaynumber = displaynumber + 1
                    displaysize = str(pygame.display.list_modes()[displaynumber])
                    for firstsel in firstsels:
                        pygame.draw.rect(screen, white, (bigbuttonx, bigbuttony, bigbuttonwidth, bigbuttonheight))
                        bigtextsurface = bigfont.render(displaysize, True, black)
                        screen.blit(bigtextsurface, (bigbuttonx, bigbuttony))
                        pygame.display.update()
                        screenwidth = int(pygame.display.list_modes()[displaynumber][0])
                        screenheight = int(pygame.display.list_modes()[displaynumber][1])
            if enter == True:
                pygame.display.set_mode((screenwidth, screenheight))

                enter = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()

















maingame()