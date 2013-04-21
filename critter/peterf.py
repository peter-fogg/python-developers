import critter
import color

class PeterF(critter.Critter):
    '''
    Just a simple test to make sure everything's working as
    intended. Oren seems to be beating me, though, so something must
    be wrong.
    '''
    def __init__(self):
        pass
    
    def fight(self, oppInfo):
        return critter.ROAR

    def getMove(self, info):
        return critter.NORTH

    def getColor(self):
        return color.BLUE

    def getChar(self):
        return 'P'

    def fightOver(self, won, oppMove):
        pass
