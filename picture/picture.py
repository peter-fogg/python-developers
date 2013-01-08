#!/usr/bin/env python3
import Image
import tkinter

class Picture():

    def __init__(self, width, height):
        self.image = Image.new('RGB', (width, height))
    
