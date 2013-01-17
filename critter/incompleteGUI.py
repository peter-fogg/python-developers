#!/usr/bin/env python3
import tkinter as tk
import critter_main
import color

EMPTY_CHAR = '.'

class CritterGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.grid()

        self.canvas = tk.Canvas(self.root, bg="black", height=500, width=700)
        self.canvas.configure(background='white')
        self.canvas.grid(columnspan = 25, rowspan = 10, sticky = 'W')

        self.classes_label = tk.Label(self.root, text='Classes(Alive+Kill=Total):')
        self.classes_label.grid(column = 25, row = 0, columnspan = 3)

        self.speed_label = tk.Label(self.root, text='Speed:')
        self.speed_label.grid(column = 0, row = 10)

        self.speed_var = tk.IntVar()
        self.speed_var.set(10)
        self.scale = tk.Scale(self.root, variable = self.speed_var, orient='horizontal',
                              length = 100, sliderlength = 20)
        self.scale.grid(column = 1, row = 10)

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

        #Bug with the radiobuttons: Does not automatically select rb1.
        #When hovering over the three options, all three appear to be selected.
        #Once one of the three is selected, problem never shows up again.
        self.v=tk.IntVar()
        
        #According to online sources the following line can solve the problem, 
        #but it does not really work.
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

        # Actually make Critters.
        self.model = critter_main.CritterModel(50, 60)
        for critter in critter_main.get_critters():
            self.model.add(critter, 25)
    
    def draw_char(self, char, color, x, y):
        """
        Displays a single char at position (x, y) on the canvas.

        TODO: make sure the positioning is actually correct (it's probably not).
        """
        self.canvas.create_text((x*15 + 5, y*15 + 5), text=char, fill=color_to_hex(color),
                                font=('Courier New', 15))
    
    def update(self):
        """
        Updates the GUI with the appropriate characters and colors from
        the critter simulation. This should be called by Tk, not directly
        from our code.
        """
        for x in range(self.model.width):
            for y in range(self.model.height):
                critter = self.model.grid[x][y]
                if critter:
                    self.draw_char(critter.getChar(), critter.getColor(), x, y)
                else:
                    self.draw_char(EMPTY_CHAR, color.BLACK, x, y)
        self.model.update()
        self.root.after(int(5000/self.speed_var.get()), self.update)
    
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
    c = CritterGUI()
    c.run()

if __name__ == '__main__':
    main()
