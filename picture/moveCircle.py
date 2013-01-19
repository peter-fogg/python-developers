from tkinter import *
from random import *

class GUI(Frame):
    def __init__(self, WIDTH, HEIGHT):
        Frame.__init__(self, None)
        self.grid()

        global canvas
        canvas = Canvas(self, width=WIDTH, height=HEIGHT, background="white")
        canvas.grid()

    def drawCircle(self, x, y, r):
        self.shape = canvas.create_oval(x-r, y-r, x+r, y+r, fill = "black")
        self.x = x
        self.y = y
        self.r = r

    def Animate(self):
        self.move()
        canvas.update()
        canvas.after(1, self.Animate)

    def move(self):
        canvas.coords(self.shape, self.x - self.r + 1,
                      self.y - self.r + 1,
                      self.x + self.r + 1,
                      self.y + self.r + 1)
        self.x = self.x + 1
        self.y = self.y + 1

def main():
    window = GUI(500, 500)
    window.drawCircle(20, 20, 10)
    window.Animate()
    window.mainloop()

main()
