from svg_parser import parsesvg
from annotationMaker import description, name
from turtle import *
import os
import time



#Control variables for centering feature
high_x = 0
high_y = 0
low_x = 0
low_y = 0
low = [1000, 1000]
high = [0, 0]

#Adjustable Variables ('file_dir' variable needs to be relative or absolute path), increase 'tracer(100)' value to speed up drawing, change printToFile to True to print raw turtle commands to textFile directory
speed(0)
hideturtle()
circle_lines = 100
tracer(10000)
file_dir = "svgTool/eva01.svg"
progress_digits = 1
pixelart_size_multipler = 2.2
printToFile = False
textFile = "svgTool/textFile.py"

#Parsing function
objects = parsesvg(file_dir)

#Annontation Settings
annotations = True
if annotations == True:
    titleDesc = "EVA-01: A Mechanical Monster"
    message = "Pixel art of a character from the \n1989 anime \'Neon Genesis Evangelion\'"
    coordinates = [-600, 300]
    descriptionTitle = description(message, titleDesc, coordinates)
    nameDesc = "David Comor"
    nameCoordinates = [-600, -350]
    nameTitle = name(nameDesc, nameCoordinates)

#Opening testfile for writing
if printToFile:
    textFile = open(textFile, "w")  
    textFile.write("from turtle import * \n")
    textFile.write("speed(0) \n")
    textFile.write("tracer(10000) \n \n")
    lineCounter = 0
    textFile.write("def drawSquare(fillColor, width, height): \n    color(\"black\", fillColor) \n    begin_fill() \n    pendown() \n    forward(width) \n    right(90) \n    forward(height) \n    right(90) \n    forward(width) \n    right(90) \n    forward(height) \n    right(90) \n    penup() \n    end_fill() \n\n")

#Finds the bottom left and top right corners of the file to be used later in the centering
for object in objects:
    if object.name == 'polygon':
        for point in range(len(object.coordinates)):
            if object.coordinates[point][0] >= high[0]:
                high[0] = object.coordinates[point][0]
            if object.coordinates[point][0] <= low[0]:
                low[0] = object.coordinates[point][0]

            if object.coordinates[point][1] >= high[1]:
                high[1] = object.coordinates[point][1]
            if object.coordinates[point][1] <= low[1]:
                low[1] = object.coordinates[point][1]
    elif object.name == 'rectangle':
        total_coordinates = [[object.xcoordinate, object.ycoordinate], [object.xcoordinate + object.width, object.ycoordinate], [object.xcoordinate + object.width, object.ycoordinate - object.height], [object.xcoordinate, object.ycoordinate - object.height]]
        for coordinate in total_coordinates:
            if coordinate[0] >= high[0]:
                high[0] = coordinate[0]
            if coordinate[0] <= low[0]:
                low[0] = coordinate[0]

            if coordinate[1] >= high[1]:
                high[1] = coordinate[1]
            if coordinate[1] <= low[1]:
                low[1] = coordinate[1]

if printToFile:
    adjustedX = high[0] / 2
    adjustedY = high[1] / 2 * -1
    textFile.write("goto({adjustedX}, {adjustedY}) \n".format(adjustedX=adjustedX, adjustedY=adjustedY))
    textFile.write("setheading(180) \n \n")

#Drawing loop
startTime = time.time()
for object in objects:
    if object.fill != 'none' and object.fill != None and object.stroke != None:
        color(object.stroke, object.fill)
        begin_fill()
    elif object.stroke != None and object.fill == None:
        color(object.stroke)
    elif object.fill != None and object.fill != 'none':
        color(object.fill, object.fill)
        begin_fill()
    if object.name == "polygon":
        for point in range(len(object.coordinates)):
            if progress_digits == 0:
                title(f'Drawing \"{os.path.basename(file_dir)}\"; {round(objects.index(object)/len(objects)*100)}%; Object #{objects.index(object)}/{len(objects)-1} ({round(point/len(object.coordinates)*100)}%); Object Shape: {object.name}')
            else: 
                title(f'Drawing \"{os.path.basename(file_dir)}\"; {round(objects.index(object)/len(objects)*100, progress_digits)}%; Object #{objects.index(object)}/{len(objects)-1} ({round(point/len(object.coordinates)*100, progress_digits)}%); Object Shape: {object.name}')
            
            if point == 0:
                penup()
                goto((object.coordinates[point][0] - high[0]/2), -(object.coordinates[point][1] - high[1]/2))
            else:
                pendown()
                goto((object.coordinates[point][0] - high[0]/2), -(object.coordinates[point][1] - high[1]/2))
    elif object.name == "circle":
        penup()
        goto(object.x_coord - high[0]/2, -(object.y_coord - high[1]/2 + object.radius))
        pendown()
        circle(object.radius, steps=circle_lines)
    elif object.name == "rectangle":
        if printToFile == False:
            if progress_digits == 0:
                title(f'Drawing \"{os.path.basename(file_dir)}\"; {round(objects.index(object)/len(objects)*100)}%; Object #{objects.index(object)}/{len(objects)-1}; Object Shape: {object.name}')
            else: 
                title(f'Drawing \"{os.path.basename(file_dir)}\"; {round(objects.index(object)/len(objects)*100, progress_digits)}%; Object #{objects.index(object)}/{len(objects)-1}; Object Shape: {object.name}')

            if objects.index(object) == 0:
                penup()
            if object.fill != None and object.fill != "none":
                #color(object.fill)
                color("black", object.fill)
            else:
                color("black")
            begin_fill()
            goto((object.xcoordinate - high[0]/2) * pixelart_size_multipler, -(object.ycoordinate - high[1]/2) * pixelart_size_multipler)
            pendown()
            forward(object.width * pixelart_size_multipler)
            right(90)
            forward(object.height * pixelart_size_multipler)
            right(90)
            forward(object.width * pixelart_size_multipler)
            right(90)
            forward(object.height * pixelart_size_multipler)
            right(90)
            penup()
        elif printToFile == True:
            try:
                if y != -(object.ycoordinate - high[1]/2):
                    lineCounter += 1
                    textFile.write("\n")
                    textFile.write("#Line {lineCounter} \n".format(lineCounter=lineCounter))
            except NameError:
                textFile.write("#Line {lineCounter} \n".format(lineCounter=lineCounter))
            
            try:
                oldX = x
                oldY = y
            except NameError:
                pass
            x = object.xcoordinate-high[0]/2
            y =-(object.ycoordinate - high[1]/2)
            objectWidth = object.width
            objectHeight = object.height
            """
            if objects.index(object) == 0:
                textFile.write("penup() \n")
            if object.fill != None and object.fill != "none":
                #color(object.fill)
                objectFill = object.fill
                textFile.write("color(\"black\", \"{objectFill}\") \n".format(objectFill=objectFill))
            else:
                textFile.write("color(\"black\") \n")
            textFile.write("begin_fill() \n")
            textFile.write("goto({x} * {pixelart_size_multipler}, {y} * {pixelart_size_multipler}) \n".format(x=x, pixelart_size_multipler=pixelart_size_multipler, y=y,))
            textFile.write("pendown() \n")
            textFile.write("forward({objectWidth} * {pixelart_size_multipler}) \n".format(objectWidth=objectWidth, pixelart_size_multipler=pixelart_size_multipler))
            textFile.write("right(90) \n")
            textFile.write("forward({objectHeight} * {pixelart_size_multipler}) \n".format(objectHeight=objectHeight, pixelart_size_multipler=pixelart_size_multipler))
            textFile.write("right(90) \n")
            textFile.write("forward({objectWidth} * {pixelart_size_multipler}) \n".format(objectWidth=objectWidth, pixelart_size_multipler=pixelart_size_multipler))
            textFile.write("right(90) \n")
            textFile.write("forward({objectHeight} * {pixelart_size_multipler}) \n".format(objectHeight=objectHeight, pixelart_size_multipler=pixelart_size_multipler))
            textFile.write("right(90) \n")
            textFile.write("penup() \n")
            textFile.write("end_fill() \n \n")
            """
            coordinate = [x * pixelart_size_multipler, y * pixelart_size_multipler]
            fillColor = object.fill
            width = object.width * pixelart_size_multipler
            height = object.height * pixelart_size_multipler

            try:
                if oldX != x:
                    textFile.write("forward({width}) \n".format(width=width))
                if oldY != y:
                    dist = high[0] - low[0]
                    textFile.write("setheading(90) \nforward({height}) \nsetheading(0) \nforward({dist}) \nsetheading(180) \n".format(height=height, dist=dist))
            except NameError:
                pass
                
            textFile.write("drawSquare(\"{fillColor}\", {width}, {height}) \n".format(fillColor=fillColor, width=width, height=height))
            
    if object.fill != 'none':
        end_fill()
    end_fill()

timeElapsed = round(time.time() - startTime)

if printToFile == True:
    textFile.write("exitonclick()")
    textFile.close()

if annotations == True:
    descriptionTitle.drawDescription()
    nameTitle.drawName()

title(f'Finished \"{os.path.basename(file_dir)}\"; Time Elapsed: {timeElapsed} seconds')
update()
exitonclick()