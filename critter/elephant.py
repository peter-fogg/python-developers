import critter
import color

class Elephant(critter.Critter):

    def __init__(self, steps):
        self.steps = steps
        self.count = 0
        self.direction = critter.EAST

    def fight(self, opponent):
        if opponent == 'T':
            return critter.ROAR
        return critter.POUNCE

    def getColor(self):
        return color.GRAY

    def getMove(self, info):
        if self.count % self.steps == 0:
            if self.direction == critter.SOUTH:
                self.direction = critter.WEST
            elif self.direction == critter.WEST:
                self.direction = critter.NORTH
            elif self.direction == critter.NORTH:
                self.direction = critter.EAST
            else:
                self.direction = critter.SOUTH
        self.count += 1
        return self.direction

    def getChar(self):
        return 'E'
