from tkinter import *

class GUI(Frame):
    def __init__(self, WIDTH, HEIGHT):
        Frame.__init__(self, None)
        self.grid()

        MenuBar = Frame(self)
        MenuBar.grid(row = 0, column = 0, sticky=W)
        
        QuitButton = Button(MenuBar, text="Quit", command = self.quit)
        QuitButton.grid(row = 0, column = 0)
        
        global canvas
        canvas = Canvas(self, width=WIDTH, height=HEIGHT, background="white")
        canvas.grid(row=1, column=0)

    def drawCircle(self, x, y, r):
        circle = canvas.create_oval(x-r, y-r, x+r, y+r, fill = "black")
        return circle

def moveby(shape, dx, dy):
    canvas.move(shape, dx, dy)

def moveto(shape, x1, y1, x2, y2):
    canvas.coords(shape, x1, y1, x2, y2)

def display():
    canvas.update()

def delay(millisecond):
    canvas.after(millisecond)

def main():
    window = GUI(500, 500)
    circle1 = window.drawCircle(20, 20, 10)
    circle2 = window.drawCircle(480, 20, 10)
    display()
    delay(2000)
    for x in range(0, 470):
        moveby(circle1, 1, 1)
        moveby(circle2, -1, 1)
        display()
        delay(20)
    window.mainloop()

main()
