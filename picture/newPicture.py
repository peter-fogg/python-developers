from tkinter import *
import math

class Picture():
    def __init__(self, param, TITLE=None):
        self.root = Tk()
        self.root.iconbitmap(default='favicon.ico')
        if TITLE!=None:
            self.root.wm_title(TITLE)
        
        self.frame = Frame(self.root, None, borderwidth=0)
        self.frame.grid()

        global canvas
        # Check if parameter is the right type, because we can't
        # overload functions
        if isinstance(param, tuple) and len(param) == 2:
            canvas = Canvas(self, width=param[0], height=param[1],
                            background="white", bd=0, 
                            highlightthickness=0)
            canvas.grid()
        elif isinstance(param, str):
            self.image = PhotoImage(file=param)
            canvas = Canvas(self, width=self.image.width(),
                            height=self.image.height(), bd=0, 
                            highlightthickness=0)
            canvas.grid()
            canvas.create_image(0, 0, image=self.image)
        else:
            raise TypeError('Parameter to Picture() should be' +
                        'string of a .gif/pgm/ppm file name or 2-tuple!')

        global outlineColor
        outlineColor = "black"

        global fillColor
        fillColor = "white"

        global penWidth
        penWidth = 1

        global pen_position
        pen_position= (0, 0)

        global pen_rotation
        pen_rotation = 0

    def setPosition(self, x, y):
        global pen_position
        pen_position = (x, y)

    def setPenX(self, x):
        global pen_position
        pen_position = (x, pen_position[1])

    def setPenY(self, y):
        global pen_position
        pen_position = (pen_position[0], y)

    def getPosition(self):
        return pen_position

    def rotate(self, theta):
        global pen_rotation
        pen_rotation += theta
        pen_rotation %= 360

    def setDirection(self, theta):
        self.pen_rotation = theta
        self.pen_rotation %= 360

    def getDirection(self):
        return pen_rotation

    def drawForward(self, distance):
        global pen_position
        radian = math.radians(pen_rotation)
        startX = pen_position[0]
        startY = pen_position[1]
        endX = startX + math.cos(radian)*distance
        endY = startY + math.sin(radian)*distance
        end = (endX, endY)
        pen_position = end
        return self.drawLine(startX, startY, endX, endY)

    def setFillColor(self, color):
        global fillColor
        fillColor = color_to_hex(color)

    def getFillColor(self):
        return fillColor

    def setOutlineColor(self, color):
        global outlineColor
        outlineColor = color_to_hex(color)

    def getOutlineColor(self):
        return outlineColor

    def setPenWidth(self, width):
        global penWidth
        penWidth = width

    def getPenWidth(self):
        return penWidth

    def drawOval(self, x, y, hrad, vrad):
        return Oval(x + 3, y + 3, hrad, vrad, False)

    def drawOvalFill(self, x, y, hrad, vrad):
        return Oval(x + 3, y + 3, hrad, vrad, True)

    def drawCircle(self, x, y, r):
        return Circle(x + 3, y + 3, r, False)
    
    def drawCircleFill(self, x, y, r):
        return Circle(x + 3, y + 3, r, True)

    def drawRect(self, x, y, w, h):
        return Rectangle(x + 3, y + 3, w, h, False)
    
    def drawRectFill(self, x, y, w, h):
        return Rectangle(x + 3, y + 3, w, h, True)

    def drawSquare(self, x, y, side):
        return Square(x + 3, y + 3, side, False)

    def drawSquare(self, x, y, side):
        return Square(x + 3, y + 3, side, True)

    def drawPolygon(self, vertices):
        return Polygon(map(lambda x: x + 3, vertices), False)

    def drawPolygonFill(self, vertices):
        return Polygon(map(lambda x: x + 3, vertices), True)

    def drawLine(self, x1, y1, x2, y2):
        return Line(x1 + 3, y1 + 3, x2 + 3, y2 + 3)

    def drawText(self, x, y, TEXT, font_name, font_size):
        return Text(x + 3, y + 3, TEXT, font_name, font_size)

    def changeCanvasSize(self, newWidth, newHeight):
        canvas.config(width=newWidth, height=newHeight)

    def display(self):
        canvas.update()

    def delay(self, millisecond):
        canvas.after(millisecond)

    def pixel(self, x, y, color):
        canvas.create_line(x + 3, y + 3, x + 4, y + 4, fill=color_to_hex(color))

class Shape:
    def __init__(self, vertices):
        self.vertices = vertices
        self.my_shape = None

    def getLocation(self):
        return (self.vertices[0][0], self.vertices[0][1])

    def changeFillColor(self, color):
        canvas.itemconfigure(self.my_shape, fill = color_to_hex(color))

    def changeOutlineColor(self, color):
        canvas.itemconfigure(self.my_shape, outline = color_to_hex(color))

    def moveby(self, dx, dy):
        canvas.move(self.my_shape, dx, dy)
        for point in self.vertices:
            point[0] = point[0] + dx
            point[1] = point[1] + dy

    def moveto(self, x, y):
        [a, b] = self.vertices[0]
        dx = x - a
        dy = y - b
        self.moveby(dx, dy)

class Rectangle(Shape):
    def __init__(self, x, y, w, h, fill=False):
        Shape.__init__(self, [[x, y], [x+w, y+h]])
        if fill==True:
            self.my_shape = canvas.create_rectangle(x, y, x+w, y+h, fill=fillColor,
                                                outline=outlineColor,
                                                width=penWidth)
        else:
            self.my_shape = canvas.create_rectangle(x, y, x+w, y+h, 
                                                outline=outlineColor,
                                                width=penWidth)



class Square(Rectangle):
    def __init__(self, x, y, side, fill):
        Rectangle.__init__(self, x, y, x+side, y+side, fill)

class Oval(Shape):
    def __init__(self, x, y, hrad, vrad, fill=False):
        Shape.__init__(self,[[x-hrad, y-vrad], [x+hrad, y+vrad]])
        if fill==True:
            self.my_shape = canvas.create_oval(x-hrad, y-vrad, x+hrad, y+vrad,
                                           fill=fillColor, outline=outlineColor,
                                           width=penWidth)
        else:
            self.my_shape = canvas.create_oval(x-hrad, y-vrad, x+hrad, y+vrad,
                                           outline=outlineColor,
                                           width=penWidth)

class Circle(Oval):
    def __init__(self, x, y, r, fill):
        Oval.__init__(self, x, y, r, r, fill)

class Polygon(Shape):
    def __init__(self, vertices, fill=False):
        Shape.__init__(self, vertices)
        if fill==True:
            self.my_shape = canvas.create_polygon(vertices, fill=fillColor,
                                              outline=outlineColor,
                                              width=penWidth)
        else:
            self.my_shape = canvas.create_polygon(vertices, 
                                              outline=outlineColor,
                                              width=penWidth)

class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        Shape.__init__(self, [[x1, y1], [x2, y2]])
        self.my_shape = canvas.create_line(x1, y1, x2, y2,
                                           fill=outlineColor, width=penWidth)

#font_name and font_size are STRINGS, e.g. "Helvectica" and "16"
class Text(Shape):
    def __init__(self, x, y, TEXT, font_name, font_size):
        Shape.__init__(self, [[x, y]])
        self.my_shape = canvas.create_text(x, y, text = TEXT,
                                           font=(font_name, font_size))


                                           
def color_to_hex(color):
    return '#%02x%02x%02x'.upper() % (color[0], color[1], color[2])

