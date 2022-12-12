import pygame
import json
import os


pygame.init()

def where_json(file_name):
    return os.path.exists(file_name)

if where_json('data\screen.json'):
    with open("data\screen.json", 'r') as file:
        nowscreenwidhei = pygame.display.list_modes()[0]
        screenwidhei = json.load(file)
        screenwidth = screenwidhei[0]
        screenheight = screenwidhei[1]
        if nowscreenwidhei[0] < screenwidhei[0] or nowscreenwidhei[1] < screenwidhei[1]:
            screenwidhei = pygame.display.list_modes()[0]
            with open("data\screen.json", "w") as outfile:
                json.dump(screenwidhei, outfile)

else:
    screenwidhei = pygame.display.list_modes()[0]
    with open("data\screen.json", "w") as outfile:
        json.dump(screenwidhei, outfile)


scrbutsetting = False
screenwidth = screenwidhei[0]
screenheight = screenwidhei[1]
mainbuttonheight = screenheight / 7
mainfontsize = int(mainbuttonheight * 0.9)
mainbuttonx = screenwidth / 10
mainbuttonwidth = screenwidth - mainbuttonx * 2
bigbuttonheight = mainbuttonheight * 1.3
bigfontsize = int(bigbuttonheight * 0.9)
bigbuttonwidth = mainbuttonwidth * 1.15
bigbuttonx = screenwidth / 2 - bigbuttonwidth / 2
bigbuttonbasicy = mainbuttonheight * 1.5 - bigbuttonheight / 2
white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode((screenwidth, screenheight))

def scrsetall():
    mainbuttonheight = screenheight / 7
    mainfontsize = int(mainbuttonheight * 0.9)
    mainbuttonx = screenwidth / 10
    mainbuttonwidth = screenwidth - mainbuttonx * 2
    bigbuttonheight = mainbuttonheight * 1.3
    bigfontsize = int(bigbuttonheight * 0.9)
    bigbuttonwidth = mainbuttonwidth * 1.15
    bigbuttonx = screenwidth / 2 - bigbuttonwidth / 2
    bigbuttonbasicy = mainbuttonheight * 1.5 - bigbuttonheight / 2
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen = pygame.display.set_mode((screenwidth, screenheight))

while scrbutsetting:
    scrbutsetting = False   



