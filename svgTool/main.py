from svg_parser import parsesvg
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

#Adjustable Variables ('file_dir' variable needs to be relative or absolute path), increase 'tracer(100)' value to speed up drawing
speed(0)
hideturtle()
circle_lines = 100
tracer(10)
file_dir = "svgTool/example4.svg"
progress_digits = 1
pixelart_size_multipler = 100

#Parsing function
objects = parsesvg(file_dir)

#Sets window title to filename
"""
Canvas Resizing code, useless with centering feature
canvas = getcanvassize("School/Python/turtle_library/shapes.svg").split()
screensize(float(canvas[0]), float(canvas[1]))
"""

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
                title(f'Drawing \"{os.path.basename(file_dir)}\"; {round(objects.index(object)/len(objects)*100)}%; Object #{objects.index(object)}/{len(objects)-1} ({round(point/len(object.coordinates)*100)}%)')
            else: 
                title(f'Drawing \"{os.path.basename(file_dir)}\"; {round(objects.index(object)/len(objects)*100, progress_digits)}%; Object #{objects.index(object)}/{len(objects)-1} ({round(point/len(object.coordinates)*100, progress_digits)}%)')
            
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
        if objects.index(object) == 0:
            penup()
        if object.fill != None and object.fill != "none":
            color(object.fill)
        else:
            color("black")
        begin_fill()
        goto((object.xcoordinate - high[0]/2) * pixelart_size_multipler, -(object.ycoordinate - high[0]/2) * pixelart_size_multipler)
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
    if object.fill != 'none':
        end_fill()
    end_fill()

timeElapsed = round(time.time() - startTime)

title(f'Finished \"{os.path.basename(file_dir)}\"; Time Elapsed: {timeElapsed} seconds')
update()
exitonclick()