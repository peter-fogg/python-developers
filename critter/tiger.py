import color
import critter
import random

class Tiger(critter.Critter):

    def __init__(self):
        self.count = 0
        self.orange = True
        self.direction = critter.WEST
    
    def fight(self, opponent):
        return critter.ROAR

    def getColor(self):
        if self.orange:
            self.orange = False
            return color.ORANGE
        self.orange = True
        return color.BLACK

    def getMove(self, info):
        if self.count % 3 == 0:
            new_direction = random.randint(0, 3)
            if new_direction == 0:
                self.direction = critter.WEST
            elif new_direction == 1:
                self.direction = critter.EAST
            elif new_direction == 2:
                self.direction = critter.NORTH
            else:
                self.direction = critter.SOUTH
        self.count += 1
        return self.direction

    def getChar(self):
        return 'T'
