import critter

class Mouse(critter.Critter):

    def __init__(self, color):
        self.color = color
        self.east = True
    
    def fight(self, opponent):
        return critter.SCRATCH

    def getColor(self):
        return self.color

    def getMove(self, info):
        if self.east:
            self.east = False
            return critter.EAST
        self.east = True
        return critter.SOUTH
    
    def getChar(self):
        return 'M'
