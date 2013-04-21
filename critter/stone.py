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

    # we don't have a fightOver method here, because a 
    # Stone doesn't do anything with this information
    # this method is called by the client prog when a fight is over
    # since the client prog knows who won the fight, when it calls
    # this method, it passes in true for the iWon parameter if this
    # critter won the fight, and false otherwise
    # oppWeapon is the opponent's weapon (ROAR, POUNCE, or SCRATCH)
    # oppColor is the opponent's color
    # the purpose of this information is to allow you to learn strategies