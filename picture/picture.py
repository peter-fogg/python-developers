#!/usr/bin/env python3
import Image
import ImageDraw
import tkinter

class Picture():
    
    def __init__(self, param):
        # Check if parameter is the right type, because we can't
        # overload functions
        if isinstance(param, tuple) and len(param) == 2:
            self.image = Image.new('RGB', (param))
        elif isinstance(param, str):
            self.image = Image.open(param)
        else:
            raise TypeError('Parameter to Picture() should be a string or 2-tuple!')
        # Default values for pen
        self.pen_color = (0, 0, 0)
        self.pen_position = (0, 0)
        self.pen_width = 1.0
        self.draw = ImageDraw.Draw(self.image)
        
        self.pixel = self.image.load()
    
    def getWidth(self):
        return self.image.size[0]
    
    def getHeight(self):
        return self.image.size[1]
    
    def display(self):
        pass

    def close(self):
        pass
    
    def getPixelColor(self, x, y):
        return self.pixel[x, y]
    
    def getPixelRed(self, x, y):
        return self.pixel[x, y][0]
    
    def getPixelBlue(self, x, y):
        return self.pixel[x, y][1]
    
    def getPixelGreen(self, x, y):
        return self.pixel[x, y][2]
    
    def setPixelColor(self, x, y, r, g, b):
        self.pixel[x, y] = (r, g, b)
        
    def setPixelRed(self, x, y, val):
        green = self.pixel[x, y][1]
        blue = self.pixel[x, y][2]
        self.pixel[x, y] = (val, green, blue)
    
    def setPixelBlue(self, x, y, val):
        red = self.pixel[x, y][0]
        green = self.pixel[x, y][1]
        self.pixel[x, y] = (red, green, val)
    
    def setPixelGreen(self, x, y, val):
        red = self.pixel[x, y][0]
        blue = self.pixel[x, y][2]
        self.pixel[x, y] = (red, val, blue)
    
    def setPenColor(self, r, g, b):
        self.pen_color = (r, g, b)
    
    def setPenX(self, x):
        self.pen_position = (x, self.pen_position[1])

    def setPenY(self, y):
        self.pen_position = (self.pen_position[0], y)
    
    def rotate(self, theta):
        self.pen_rotation += theta
        self.pen_rotation %= 360
    
    def setDirection(self, theta):
        self.pen_rotation = theta
        self.pen_rotation %= 360

    def getDirection(self):
        return self.pen_rotation
    
    def drawForward(self, distance):
        pass

    def drawCircle(self, x, y, radius):
        self.draw.ellipse((x-radius/2, y-radius/2,
                           x+radius/2, y+radius/2),
                          outline=self.pen_color)

    def drawCircleFill(self, x, y, radius):
        self.draw.ellipse((x-radius/2, y-radius/2,
                           x+radius/2, y+radius/2),
                          fill=self.pen_color)
    
    def fillPoly(self, xs, ys):
        self.draw.polygon(zip(xs, ys), fill=self.pen_color)
        
    def drawPoly(self, xs, ys):
        self.draw.polygon(zip(xs, ys), outline=self.pen_color)
    
    def drawRectFill(self, x, y, w, h):
        self.draw.polygon(((x, y), (x+w, y+h)), fill=self.pen_color)

    def drawRect(self, x, y, w, h):
        self.draw.polygon(((x, y), (x+w, y+h)), outline=self.pen_color)
    
    def drawString(self, x, y, string):
        self.draw((x, y), string, fill=self.pen_color)

    def writeFile(self, filename):
        self.image.save(filename)
