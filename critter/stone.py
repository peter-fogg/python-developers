import critter
import color

class Stone(critter.Critter):

    def fight(self, opponent):
        return critter.ROAR
    
    def getColor(self):
        return color.GRAY
    
    def getMove(self, info):
        return critter.CENTER

    def getChar(self):
        return 'S'
