from tkinter import *

class Animate(Frame):
    def __init__(self, param):
        Frame.__init__(self, None)
        self.grid()

        global canvas
        # Check if parameter is the right type, because we can't
        # overload functions
        if isinstance(param, tuple) and len(param) == 2:
            canvas = Canvas(self, width=param[0], height=param[1],
                            background="white")
            canvas.grid()
        elif isinstance(param, str):
            self.image = PhotoImage(file=param)
            canvas = Canvas(self, width=self.image.width(),
                            height=self.image.height())
            canvas.grid()
            canvas.create_image(0, 0, image=self.image, anchor=NW)
        else:
            raise TypeError('Parameter to AnimatePicture() should be' +
                        'string of a .gif/pgm/ppm file name or 2-tuple!')

        global outlineColor
        outlineColor = "black"

        global fillColor
        fillColor = "white"

        global penWidth
        penWidth = 1

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

    def drawOval(self, x, y, hrad, vrad, fill):
        return Oval(x, y, hrad, vrad, fill)

    def drawCircle(self, x, y, r, fill):
        return Circle(x, y, r, fill)

    def drawRectangle(self, x, y, w, h, fill):
        return Rectangle(x, y, w, h, fill)

    def drawSquare(self, x, y, side, fill):
        return Square(x, y, side, fill)

    def drawPolygon(self, vertices, fill):
        return Polygon(vertices, fill)

    def drawLine(self, x1, y1, x2, y2):
        return Line(x1, y1, x2, y2)

    def drawText(self, x, y, TEXT, font_name, font_size):
        return Text(x, y, TEXT, font_name, font_size)

    def changeCanvasSize(self, newWidth, newHeight):
        canvas.config(width=newWidth, height=newHeight)

    def display(self):
        canvas.update()

    def delay(self, millisecond):
        canvas.after(millisecond)

    def pixel(self, x, y, color):
        canvas.create_line(x, y, x+1, y+1, fill=color_to_hex(color))

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
        if fill=="FILL":
            FILL=fillColor
        else:
            FILL=None
        Shape.__init__(self, [[x, y], [x+w, y+h]])
        self.my_shape = canvas.create_rectangle(x, y, x+w, y+h, fill=FILL,
                                                outline=outlineColor,
                                                width=penWidth)



class Square(Rectangle):
    def __init__(self, x, y, side, fill):
        Rectangle.__init__(self, x, y, x+side, y+side, fill)

class Oval(Shape):
    def __init__(self, x, y, hrad, vrad, fill=False):
        if fill=="FILL":
            FILL=fillColor
        else:
            FILL=None
        Shape.__init__(self,[[x-hrad, y-vrad], [x+hrad, y+vrad]])
        self.my_shape = canvas.create_oval(x-hrad, y-vrad, x+hrad, y+vrad,
                                           fill=FILL, outline=outlineColor,
                                           width=penWidth)

class Circle(Oval):
    def __init__(self, x, y, r, fill):
        Oval.__init__(self, x, y, r, r, fill)

class Polygon(Shape):
    def __init__(self, vertices, fill=False):
        if fill=="FILL":
            FILL=fillColor
        else:
            FILL=None
        Shape.__init__(self, vertices)
        self.my_shape = canvas.create_polygon(vertices, fill=FILL,
                                              outline=outlineColor,
                                              width=penWidth)

class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        Shape.__init__(self, [[x1, y1], [x2, y2]])
        self.my_shape = canvas.create_line(x1, y1, x2, y2,
                                           fill=outlineColor)

#font_name and font_size are STRINGS, e.g. "Helvectica" and "16"
class Text(Shape):
    def __init__(self, x, y, TEXT, font_name, font_size):
        Shape.__init__(self, [[x, y]])
        self.my_shape = canvas.create_text(x, y, text = TEXT,
                                           font=(font_name, font_size))


                                           
def color_to_hex(color):
    return '#%02x%02x%02x'.upper() % (color[0], color[1], color[2])



#Show circles at initial position for 2 secs, then move diagonally. 
def main():
    pic = Animate((500, 500))
    pic.setOutlineColor((255, 0, 0))
    print (pic.getOutlineColor())
    pic.setFillColor((0, 0, 255))
    print (pic.getFillColor())
    pic.setPenWidth(2)
    circle1 = pic.drawCircle(20, 20, 10, "FILL")
    circle2 = pic.drawCircle(480, 20, 10, "FILL")
    pic.setFillColor((255, 0, 0))
    circle3 = pic.drawCircle(250, 250, 20, "FILL")
    pic.display()
    pic.delay(2000)
    draw = True
    for x in range(0, 470):
        circle1.moveby(1, 1)
        circle2.moveto(circle2.getLocation()[0]-1,
                   circle2.getLocation()[1]+1)
        if draw == True:
            circle3.changeOutlineColor((0, 0, 255))
            circle3.changeFillColor((0, 0, 255))
            draw = False
        else:
            circle3.changeOutlineColor((255, 0, 0))
            circle3.changeFillColor((255, 0, 0))
            draw = True
        pic.display()
        pic.delay(20)
##    Super slow pixel manipulation:
##    for x in range(0, 500):
##        for y in range(0, 250):
##            pic.pixel(x, y, (255, 0, 0))
##    pic.display()

main()
