import math

class Triangle:
    name = "Triangle"
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def getArea(self):
        return 0.5 * self.base * self.height
    
class Circle:
    name = "Circle"
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi*(self.radius**2)
    
class Rectangle:
    name = "Rectangle"
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width
    
shapes = open(r"C:\Users\awall\OneDrive\Desktop\GISProgramming\topic\03\shape.txt", "r")

shapeLines = []
for x in shapes:
    shapesnew = x.split(",")
    shapesnewlen = len(shapesnew)

    counter = 0
    for y in shapesnew:
        if counter == 0:
            counter += 1
            continue

        elif counter <= (shapesnewlen - 2):
            shapesnew[counter] = int(shapesnew[counter])
            counter += 1

        else:
            shapesnew[counter] = int(shapesnew[counter][0])
            counter += 1

    shapeLines.append(shapesnew)

shapeObj = []
for x in shapeLines:
    if x[0] == "Rectangle":
        shape = Rectangle(x[1], x[2])
        shapeObj.append(shape)

    elif x[0] == "Triangle":
        shape = Triangle(x[1], x[2])
        shapeObj.append(shape)
    
    else:
        shape = Circle(x[1])
        shapeObj.append(shape)

counter = 1
for x in shapeObj:
    if x.name == "Triangle":
        print("Shape", counter, "is a Triangle with a base of", x.base, "and a height of", x.height)

    elif x.name == "Circle":
        print("Shape", counter, "is a Circle with a radius of", x.radius)

    else:
        print("Shape", counter, "is a Rectangle with a length of", x.length, "and a width of", x.width)

    print("The area of shape", counter, "is", x.getArea())
    print()
    counter += 1

shapes.close()
