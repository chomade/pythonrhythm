import pygame
from classdefall import mainbuttonx, mainbuttonheight, mainbuttonwidth, scrsetall
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


