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

setting = False
main_screen = True

font = pygame.font.Font("data\DNF.otf", intmainbuttonheight)


def resolutionscreen():
    global main_screen
    global setting
    resolution = True
    main_screen = False
    setting = False


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
    Button("screen resolution", mainbuttonx, mainbuttonheight * 1, mainbuttonwidth, mainbuttonheight, 1),
    Button("sound", mainbuttonx, mainbuttonheight * 3, mainbuttonwidth, mainbuttonheight, 3),
    Button("back", mainbuttonx, mainbuttonheight * 5, mainbuttonwidth, mainbuttonheight, 5),
]


def maingame():
    global main_screen
    global setting
    while main_screen:
        mouse = pygame.mouse.get_pos()
        for button, event in main_buttons, events:
            pygame.draw.rect(screen, white, button.rect)
            textsurface = font.render(button.name, True, black)
            screen.blit(textsurface, (mainbuttonx, mainbuttonheight * button.number))
            if button.x + button.width >= mouse[0] >= button.x and button.y + button.height >= mouse[1] >= button.y and \
                    event.type == pygame.MOUSEBUTTONDOWN:
                if mainbuttonheight * 1 <= button.y <= mainbuttonheight * 2:
                    print("1")
                elif mainbuttonheight * 5 <= button.y <= mainbuttonheight * 6:
                    screen.fill(black)
                    main_screen = False
                    setting = True
                    settinggame()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()
        pygame.display.update()


def settinggame():
    global setting
    global main_screen
    while setting:
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.MOUSEBUTTONUP
        for button in setting_buttons:
            screen.fill(black)
            pygame.draw.rect(screen, white, button.rect)
            textsurface = font.render(button.name, True, black)
            screen.blit(textsurface, (mainbuttonx, mainbuttonheight * button.number))
            if button.x + button.width >= mouse[0] >= button.x and button.y + button.height >= mouse[1] >= button.y and \
                    click[0]:
                if mainbuttonheight * 1 <= button.y <= mainbuttonheight * 2:
                    print("1")
                elif mainbuttonheight * 3 <= button.y <= mainbuttonheight * 4:
                    main_screen = False
                    setting = True
                elif mainbuttonheight * 5 <= button.y <= mainbuttonheight * 6:
                    screen.fill(black)
                    setting = False
                    main_screen = True
                    maingame()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()


maingame()

with open("data\key.json", "w") as outfile:
    json.dump(key, outfile)


class Key():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


keys = [
    Key(100, 0, (0, 0, 0))
]
