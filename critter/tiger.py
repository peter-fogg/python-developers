import critter
import color
import random

class Tiger(critter.Critter):

    def __init__(self) :
        self.moves = 0
        self.dir = Tiger.getRandomDir()
        
    def fight(self, oppInfo):
        return critter.ROAR
    
    def getColor(self):
        if self.moves % 2 == 0:
            return color.ORANGE
        return color.BLACK
    
    def getMove(self, info):
        if self.moves % 3 == 0 :
            self.dir = Tiger.getRandomDir()
        self.moves += 1
        return self.dir

    def getChar(self):
        return 'T'

    def getRandomDir() :
        r = random.randint(1,4)
        if r == 1 :
            return critter.EAST
        elif r == 2 :
            return critter.WEST
        elif r == 3 :
            return critter.NORTH
        return critter.SOUTH
    