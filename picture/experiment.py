##Experimental stuff.
##This thing cannot display image properly. It cannot draw shapes with certain pen width either.

import tkinter
from PIL import Image, ImageTk, ImageDraw

class Picture:
    def __init__(self, imageFile=None, width=None, height=None, FILL=None):

        global im
        if imageFile != None:
            try:
                im = Image.open(imageFile)
            except IOError:
                print ("What the...where is the image?")
                raise
        elif width!=None and height!= None:
            if FILL==None:
                im = Image.new('RGB', (width, height), (255, 255, 255))
            else:
                im = Image.new('RGB', (width, height), FILL) 
        else:
            print ("Hey give me the size for a new image!")

        global root, panel
        root = tkinter.Tk()
        tkimage = ImageTk.PhotoImage(im)
        panel = tkinter.Label(root, image=tkimage).pack()
        root.update()

        global pix
        pix = im.load()

        global draw
        draw = ImageDraw.Draw(im)

        global outlineColor
        outlineColor = (0, 0, 0)

        global fillColor
        if FILL != None:
            fillColor = FILL
        else:
            fillColor = (255, 255, 255)

        global penWidth
        penWidth = 1.0

    def setPenWidth(self, width):
        global penWidth
        penWidth = width

    def getPenWidth(self, width):
        global penWidth
        return penWidth

    def setOutlineColor(self, color):
        global outlineColor
        outlineColor = color

    def getOutlineColor(self):
        global outlineColor
        return outlineColor

    def setFillColor(self, color):
        global fillColor
        fillColor = color

    def getFillColor(self):
        global fillColor
        return fillColor


##Or do init pass and then use class methods
## to construct with different types of arguments


    def drawCircle(self, centerX, centerY, radius):
        global draw, fillColor, outlineColor, penWidth
        draw.ellipse((centerX-radius, centerY-radius, centerX+radius, centerY+radius), fill = fillColor, outline = outlineColor)
            
    def setPixel(self, X, Y, R, G, B):
        global pix
        pix[X, Y] = (R, G, B)

    def getPixel(self, X, Y):
        global pix
        return pix[X, Y]

    def setPixelRed(self, X, Y, R):
        global pix
        green = pix[X, Y][1]
        blue = pix[X, Y][2]
        pix[X, Y] = (R, green, blue)

    def getPixelRed(self, X, Y):
        global pix
        return pix[X, Y][0]

    def setPixelGreen(self, X, Y, G):
        global pix
        red = pix[X, Y][0]
        blue = pix[X, Y][2]
        pix[X, Y] = (red, G, blue)

    def getPixelGreen(self, X, Y):
        global pix
        return pix[X, Y][1]

    def setPixelBlue(self, X, Y, B):
        global pix
        red = pix[X, Y][0]
        green = pix[X, Y][1]
        pix[X, Y] = (red, green, B)

    def getPixelBlue(self, X, Y):
        global pix
        return pix[X, Y][2]

    def show(self):
##        global im
##        im.show()
        global root, im, panel
        tkimage.destroy()
        tkimage = ImageTk.PhotoImage(im)
        panel.config(image=tkimage)
        root.update()

    def save(self, fileName):
        global im
        im.save(fileName)
    
def main():
    #pic = Picture(None, 500, 500)
    pic = Picture("Chrysanthemum.jpg")
    
    ##the following for loop can be seen to work when background color is not white
    for x in range(10, 100):
        for y in range(10, 50):
            red = pic.getPixelRed(x, y)
            green = pic.getPixelGreen(x, y)
            blue = pic.getPixelBlue(x, y)
            grey = int((red + green + blue) / 3)
            pic.setPixel(x, y, grey, grey, grey)
    pic.show()
    print (pic.getPixelRed(400, 400))
    for x in range(300, 500):
        for y in range(300, 500):
            pic.setPixelRed(x, y, 255)
            pic.setPixelBlue(x, y, 255)
    pic.setOutlineColor((0, 0, 255))
    pic.drawCircle(100, 100, 50)
    pic.show()
    pic.save("Chrysanthemum1.jpg")

main()
