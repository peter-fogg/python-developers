import critter
import color    

class Mouse(critter.Critter):
    
    def __init__(self, color) :
        self.color = color
        self.moves = 0

    def fight(self, oppInfo):
        return critter.SCRATCH
    
    def getColor(self):
        return self.color
    
    def getMove(self, info):
        self.moves += 1
        if self.moves % 2 == 1 :
            return critter.EAST
        return critter.SOUTH

    def getChar(self):
        return 'M'