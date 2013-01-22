#!/usr/bin/env python3
import tkinter as tk
import critter_model
import critter_main
import color

EMPTY_CHAR = '.'

class CritterGUI():
    def __init__(self, model):
        self.model = model
        self.width = 15*self.model.width
        self.height = 15*self.model.height
        
        self.root = tk.Tk()
        self.root.grid()

        self.canvas = tk.Canvas(self.root, bg="white", width=self.width, height=self.height)
        self.canvas.grid(columnspan = 25, rowspan = 10, sticky = 'W')
        self.rectangle = self.canvas.create_rectangle((0, 0, self.width, self.height), fill='white', outline='white')

        self.classes_label = tk.Label(self.root, text='Classes(Alive+Kill=Total):')
        self.classes_label.grid(column = 25, row = 0, columnspan = 3)

        self.speed_label = tk.Label(self.root, text='Speed:')
        self.speed_label.grid(column = 0, row = 10)

        self.speed_var = tk.IntVar()
        self.speed_var.set(10)
        self.scale = tk.Scale(self.root, variable = self.speed_var, orient='horizontal',
                              length = 100, sliderlength = 10, from_=0, to=10)
        self.scale.grid(column = 1, row = 10)

        #Once a move is made, the text should be updated.
        self.move_count = tk.Label(self.root, text='0 moves')
        self.move_count.grid(column = 3, row = 10)
        
        self.go_button = tk.Button(self.root, text = 'Go', bg = 'green',
                                   width = 6, command = None)
        self.go_button.grid(column = 8, row = 10)

        self.stop_button = tk.Button(self.root, text = 'Stop', bg = 'red',
                                     width = 6, command = None)
        self.stop_button.grid(column = 9, row = 10)

        self.tick_button = tk.Button(self.root, text = 'Tick', bg = 'yellow',
                                     width = 6, command = None)
        self.tick_button.grid(column = 10, row = 10)

        self.reset_button = tk.Button(self.root, text = 'Reset', bg = 'blue',
                                      width = 6, command = None)
        self.reset_button.grid(column = 11, row = 10)

        self.request_option_label = tk.Label(self.root, text = 'Accept requests:')
        self.request_option_label.grid(column = 25, row = 9, columnspan = 3)

        self.v=tk.IntVar()
        
        self.v.set(1) 

        self.rb1 = tk.Radiobutton(self.root, text='Always', variable = self.v,
                                  value = 1, command = None)
        
        self.rb2 = tk.Radiobutton(self.root, text='Ask', variable = self.v,
                                  value = 2, command = None)
        
        self.rb3 = tk.Radiobutton(self.root, text='Never', variable = self.v,
                                  value = 3, command = None)

        self.rb1.grid(column = 25, row = 10)
        self.rb2.grid(column = 26, row = 10)
        self.rb3.grid(column = 27, row = 10)
        
        # I don't know how to do the part where you display the names of all the 
        # critter classes and the number of critters alive and killed, and the
        # send and request buttons for each class, because the number of critter 
        # classes is unknown. 

    def draw_char(self, char, color, x, y):
        """
        Displays a single char at position (x, y) on the canvas.

        TODO: make sure the positioning is actually correct (it's probably not).
        """
        self.canvas.create_text((x*15 + 7.5, y*15 + 8.5), text=char, fill=color_to_hex(color),
                                font=('Courier New', -15))
    
    def update(self):
        """
        Updates the GUI with the appropriate characters and colors from
        the critter simulation. This should be called by Tk, not directly
        from our code.
        """
        # Clear screen
        self.canvas.tag_raise(self.rectangle)
        # Draw all critters
        for x in range(self.model.width):
            for y in range(self.model.height):
                critter = self.model.grid[x][y]
                if critter:
                    self.draw_char(critter.getChar(), critter.getColor(), x, y)
                else:
                    self.draw_char(EMPTY_CHAR, color.BLACK, x, y)
        self.model.update()
        # self.root.after(int(5000/self.speed_var.get()), self.update)
        self.root.after(100, self.update)
    
    def run(self):
        """Actually runs the GUI. Pretty straightforward."""
        self.update()
        self.root.mainloop()

def color_to_hex(color):
    """
    Converts RGB colors to hex string, because tkinter thought that
    passing numeric types as strings was an AWESOME idea.
    """
    return '#%02x%02x%02x'.upper() % (color.r, color.g, color.b)

def main():
    model = critter_model.CritterModel(40, 30)
    critter_main.populate_model(model)
    c = CritterGUI(model)
    c.run()

if __name__ == '__main__':
    main()
