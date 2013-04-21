import critter
import color

class OrenS(critter.Critter):
    def __init__(self):
        pass
    
    def fight(self, oppInfo):
        return critter.POUNCE

    def getMove(self, info):
        return critter.SOUTH
    
    def getColor(self):
        return color.RED

    def getChar(self):
        return 'O'

    def fightOver(self, won, oppMove):
        pass
