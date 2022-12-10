import sys
import pygame
import math
import os
import time
import json


pygame.init()

font = pygame.font.SysFont('arial', 30)

screenwidth = 800
screenheight = 450

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

mainbuttonheight = screenheight / 7
mainbuttonx = screenwidth / 10
mainbuttonwidth = screenwidth - mainbuttonx * 2

setting = False
main_screen = True

def quitgame():
    Quit = True

def resolutionscreen():
    resolution = True
    main_screen = False

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
    Button("settings", mainbuttonx, mainbuttonheight * 3, mainbuttonwidth, mainbuttonheight, 3),
    Button("exit", mainbuttonx, mainbuttonheight * 5, mainbuttonwidth, mainbuttonheight, 5),
]

setting_buttons = [
    Button("screen resolution", mainbuttonx, mainbuttonheight * 1, mainbuttonwidth, mainbuttonheight, 1),
    Button("sound", mainbuttonx, mainbuttonheight * 3, mainbuttonwidth, mainbuttonheight, 3),
    Button("exit", mainbuttonx, mainbuttonheight * 5, mainbuttonwidth, mainbuttonheight, 5),
]




while main_screen:
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for button in main_buttons:
        pygame.draw.rect(screen, white, button.rect)
        textsurface = font.render(button.name, True, black)
        screen.blit(textsurface, (mainbuttonx, mainbuttonheight * button.number))
        if button.x + button.width >= mouse[0] >= button.x and button.y + button.height >= mouse[1] >= button.y and click[0]:
            if mainbuttonheight * 1 <= button.y <= mainbuttonheight * 2:
                print("1")
            elif mainbuttonheight * 3 <= button.y <= mainbuttonheight * 4:
                main_screen = False
                setting = True
            elif mainbuttonheight * 5 <= button.y <= mainbuttonheight * 6:
                pygame.quit()
                quit()
                exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            quit()
    pygame.display.update()

while setting:
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for button in setting_buttons:
        pygame.draw.rect(screen, white, button.rect)
        if button.x + button.width >= mouse[0] >= button.x and button.y + button.height >= mouse[1] >= button.y and click[0]:
            if mainbuttonheight * 1 <= button.y <= mainbuttonheight * 2:
                print("1")
            elif mainbuttonheight * 3 <= button.y <= mainbuttonheight * 4:
                main_screen = False
                setting = True
            elif mainbuttonheight * 5 <= button.y <= mainbuttonheight * 6:
                pygame.quit()
                quit()
                exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            quit()

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

