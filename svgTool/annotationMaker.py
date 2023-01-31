from turtle import *

class description():
    messageDesc = None
    titleDesc = None
    coordinateDesc = None
    titleFont = ('Arial', 15, 'bold')
    messageFont = ('Arial', 12, 'normal')
    colorDesc = "white"

    def __init__(self, message, title, coordinate : tuple, color = "white") -> None:
        self.messageDesc = message
        self.titleDesc = title
        self.coordinateDesc = coordinate
        self.colorDesc = color
        pass

    def drawDescription(self):
        color(self.colorDesc)
        goto(self.coordinateDesc)
        setheading(0)
        write(arg=self.titleDesc, font=self.titleFont)
        goto(self.coordinateDesc)
        right(90)
        forward(35)
        setheading(0)
        write(arg=self.messageDesc, font=self.messageFont)

class name():
    nameDesc = None
    coordinateDesc = None
    nameFont = ('Arial', 15, 'normal')
    colorDesc = "white"

    def __init__(self, name, coordinate : tuple, color = "white") -> None:
        self.nameDesc = name
        self.coordinateDesc = coordinate
        self.colorDesc = color
        pass

    def drawName(self):
        color(self.colorDesc)
        goto(self.coordinateDesc)
        setheading(0)
        write(arg=self.nameDesc, font=self.nameFont)
