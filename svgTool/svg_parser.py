from turtle import *
from xml.dom import minidom


class rectangle:
    def __init__(self, name, x_coord, y_coord, width, height, fill, stroke):
        self.name = name
        self.xcoordinate = x_coord
        self.ycoordinate = y_coord
        self.width = width
        self.height = height
        self.fill = fill
        self.stroke = stroke

class polygon:
    def __init__(self, name, coordinates, fill, stroke):
        self.name = name
        self.coordinates = coordinates
        self.fill = fill
        self.stroke = stroke

class circles:
    def __init__(self, name, x_coord, y_coord, radius, fill, stroke):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.radius = radius
        self.fill = fill
        self.stroke = stroke



def parsecircle(circle_xml) -> circles:
    """
    Extracts the x and y coordinates and the radius of a circle using its XML element.
    Returns a circles object
    """
    x_coordinate = float(circle_xml.attributes['cx'].value)
    y_coordinate = float(circle_xml.attributes['cy'].value)
    radius = float(circle_xml.attributes['r'].value)

    return circles("circle", x_coordinate, y_coordinate, radius, circle_xml.attributes['fill'].value, circle_xml.attributes['stroke'].value)

def parserectangle(rectangle_xml) -> rectangle:
    """
    Extracts the x and y coordinates and the width and height of a rectangle using its XML element.
    Returns a rectangle object
    """
    try:
        x_coordinate = float(rectangle_xml.attributes['x'].value)
    except:
        x_coordinate = 0
    
    try:
        y_coordinate = float(rectangle_xml.attributes['y'].value)
    except:
        y_coordinate = 0
    width = float(rectangle_xml.attributes['width'].value)
    height = float(rectangle_xml.attributes['height'].value)

    try:
        fill = rectangle_xml.attributes['fill'].value
    except:
        fill = None
    try:
        stroke = rectangle.attributes['stroke'].value
    except:
        stroke = None

    return rectangle("rectangle", x_coordinate, y_coordinate, width, height, fill, stroke)

def parsepolygon(polygon_xml) -> polygon:
    """
    Extracts the coordinate list and the stroke and fill color of a polygon using its XML element.
    Returns a polygon object
    """
    points_str = polygon_xml.attributes['points'].value
    point_ls = [[]]
    temp_point = ""
    at_y = False
    coordinates = 0
    for x in range(len(points_str)):
        i = points_str[x]
        if i != " ":
            temp_point += i
        elif at_y == False:
            point_ls[coordinates].append(float(temp_point))
            temp_point = ""
            at_y = True
            continue
        else:
            point_ls[coordinates].append(float(temp_point))
            temp_point = ""
            at_y = False
            coordinates += 1
            point_ls.append([])
            continue
    if at_y == False:
        point_ls[coordinates].append(float(temp_point))
        at_y = True
    else:
        point_ls[coordinates].append(float(temp_point))
        temp_point = ""
        at_y = False
        coordinates += 1
    
    fill = None
    stroke = None
    
    try:
        fill = polygon_xml.attributes['fill'].value
    except:
        fill = None
    try:
        stroke = polygon_xml.attributes['stroke'].value
    except:
        stroke = None


    return polygon("polygon", point_ls, fill, stroke)


def parsesvg(file_dir : str) -> list:
    """
    Parses a .svg file and extracts all the elements.
    Returns a list of these elements
    """
    file = minidom.parse(file_dir)
    polygons = file.getElementsByTagName('polygon') + file.getElementsByTagName('polyline')
    rectangles = file.getElementsByTagName('rect')
    circles = file.getElementsByTagName('circle')
    polygon_ls = []
    rectangle_ls = []
    circle_ls = []

    styles = file.getElementsByTagName('styles')
    """
    for polygon in polygons:
        polygon_ls.append(parsepolygon(polygon))

    for rectangle in rectangles:
        rectangle_ls.append(parserectangle(rectangle))

    for circle in circles:
        circle_ls.append(parsecircle(circle))
    """
    elements = file.childNodes[0].childNodes
    print(elements[0].data)
    for element in elements:
        try:
            if element.data == '\n  ' or element.data == '\n':
                elements.pop(elements.index(element))
        except:
            continue
    
    returnable_var = []
    for element in elements:
        if element.localName == 'polygon':
            returnable_var.append(parsepolygon(element))
        elif element.localName == 'rect':
            returnable_var.append(parserectangle(element))
        elif element.localName == 'circle':
            returnable_var.append(parsecircle(element))
    
    return returnable_var
    
def getcanvassize(file_dir : str) -> list:
    """
    Extracts and returns the canvas size from a .svg file in the form of a tuple
    """
    file = minidom.parse(file_dir)
    canvas = file.getElementsByTagName('svg')

    size = canvas[0].attributes._attrs['viewBox'].value
    return size[4:]