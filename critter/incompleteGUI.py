import tkinter as tk

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.grid()

        self.canvas = tk.Canvas(self.root, bg="black", height=500, width=700)
        self.canvas.grid(columnspan = 25, rowspan = 10, sticky = 'W')

        self.classes_label = tk.Label(self.root, text='Classes(Alive+Kill=Total):')
        self.classes_label.grid(column = 25, row = 0, columnspan = 3)

        self.speed_label = tk.Label(self.root, text='Speed:')
        self.speed_label.grid(column = 0, row = 10)

        var = tk.IntVar()
        self.scale = tk.Scale(self.root, variable = var, orient='horizontal',
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
        
def main():
    c = GUI()

main()
