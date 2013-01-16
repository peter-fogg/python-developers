from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
import time

class Animation():
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
        self.pen_color = (255, 0, 0)
        self.pen_position = (0, 0)
        self.pen_width = 10
        self.pen_rotation = 0
        # Pixel data of the image
        self.pixel = self.image.load()
        # Draw object of the image
        self.draw = ImageDraw.Draw(self.image)
        # The main window, if we are displaying an image. If
        # this is None, the window is closed. Otherwise, it
        # is open.
        self.root = None

    ##
    # Display the picture.
    def display(self):
        # If we're already displaying an image, destroy it
        if self.root:
            self.frame.destroy()
            self.img = None
            self.label.destroy()
##            self.root.destroy()
##            self.root = None
        else:
            self.root = tk.Tk()
        self.frame = tk.Frame(self.root, width=self.image.size[0], height=self.image.size[1])
        self.img = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self.frame, image=self.img)
        # This line ensures that Python doesn't try to garbage collect
        # our photo, due to a bug in Tk.
        self.label.image = self.img
        self.label.pack()
        self.frame.pack()
        time.sleep(1)
        self.root.update()

    ##
    # Draw a circle.
    # @param x The x-coordinate of the center of the circle.
    # @param y The y-coordinate of the center of the circle.
    # @param radius The radius of the circle.
    def drawCircleFill(self, x, y, radius):
        self.draw.ellipse((x-radius/2, y-radius/2,
                           x+radius/2, y+radius/2),
                          fill=self.pen_color)

def main():
    pic = Animation((500, 500))
    for x in range(1, 4):
        for y in range(1, 4):
            m = 100 * x
            n = 100 * y
            pic.drawCircleFill(m, n, 30)
            pic.display()

main()
