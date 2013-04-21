import critter
import color
import random

class Alexa(critter.Critter):

    oppFights = dict()
    # want it to store: 'OppCritterName', [ROARS, POUNCES, SCRATCHES]
    Alexas = []
    num_wins = 0

    def __init__(self) :
        self.moves = 0
        self.opp = None
        self.oppColor = color.GRAY
        self.oppChar = 'S'
        self.position = (0,0)
        Alexa.Alexas.append( self )
        
    def fight(self, oppInfo):
        self.oppChar = oppInfo.char
        self.oppColor = oppInfo.color
        self.opp = oppInfo.getNeighbor(critter.CENTER)
        
        if self.opp not in Alexa.oppFights : # haven't seen this opponent before
            Alexa.oppFights[self.opp] = [0,0,0]
        
        standardDefense = Alexa.beatDefaultCritters(self.opp)
        if standardDefense != None : # deal with known critters first
            return standardDefense

        fights = Alexa.oppFights[self.opp]
        if fights[2] >= fights[0] and fights[2] >= fights[1] : # max is SCRATCH
            return critter.ROAR
        elif fights[0] >= fights[2] and fights[0] >= fights[1] : # max is ROAR
            return critter.POUNCE
        return critter.SCRATCH
    
    
    def getColor(self):
        if self.moves % 5 == 0 :
            return color.RED
        elif self.moves % 5 == 1 :
            return color.ORANGE
        elif self.moves % 5 == 2 :
            return color.YELLOW
        elif self.moves % 5 == 3 :
            return color.BLUE
        else :
            return color.PURPLE
    
    def getMove(self, info):
        self.moves += 1
        
        if self.moves >= 200 : # start the sweep
            if self.moves % 2 == 0 :
                return critter.SOUTH
            else :
                return critter.EAST
        # always avoid other Alexa's if you can
        if self.moves >= 50 : # move towards the column of your index
            if info.x != Alexa.Alexas.index(self) :
                return Alexa.avoidAlexas(info, critter.EAST)
            elif info.y != (Alexa.Alexas.index(self)%2) :
                return Alexa.avoidAlexas(info, critter.NORTH)
            else :
                return critter.CENTER
            
                
        self.position = (info.x + 1, info.y)
        if (self.moves) % 5 == 0 :
            return Alexa.avoidAlexas( info, critter.EAST )
        if Alexa.seekDeath( info, critter.EAST ) != None :
            return critter.EAST
        elif Alexa.seekDeath( info, critter.SOUTH) != None :
            return critter.SOUTH
        elif Alexa.seekDeath( info, critter.WEST) != None :
            return critter.WEST
        elif Alexa.seekDeath( info, critter.NORTH )!= None :
            return critter.NORTH
        return critter.CENTER

    def getChar(self):
        if self.moves % 5 == 0 :
            return 'A'
        elif self.moves % 5 == 1 :
            return 'L'
        elif self.moves % 5 == 2 :
            return 'E'
        elif self.moves % 5 == 3 :
            return 'X'
        else :
            return 'A'

    def getRandomDir() :
        return critter.SOUTH
    
    def fightOver(self, won, oppFight ):
        if won:
            Alexa.num_wins += 1
        else:
            Alexa.num_wins -= 1
            
        if oppFight == critter.SCRATCH:
            Alexa.oppFights[self.opp][2] += 1
        elif oppFight == critter.ROAR:
            Alexa.oppFights[self.opp][0] += 1
        else:
            Alexa.oppFights[self.opp][1] += 1
            
        if not won :
            Alexa.Alexas.remove( self )

    def avoidAlexas( info, dir ) :
        if info.getNeighbor( dir ) != "Alexa" :
            return dir
        if info.getNeighbor( critter.EAST) != "Alexa" :
            return critter.EAST
        elif info.getNeighbor( critter.SOUTH ) != "Alexa" :
            return critter.SOUTH
        elif info.getNeighbour( critter.WEST ) != "Alexa" :
            return critter.WEST
        elif info.getNeighbor( critter.NORTH ) != "Alexa" :
            return critter.NORTH
        return critter.CENTER
    
    def seekDeath( info, dir ) :
        n = info.getNeighbor( dir )
        if n == "Stone" or n == "Mouse" or n == "Tiger" or n == "Elephant" :
            return dir
        else :
            return None
        
    def beatDefaultCritters( opp ) :
        if opp == "Stone" :
            return critter.POUNCE # Stones ROAR, so we beat them with a POUNCE
        elif opp == "Mouse" :
            return critter.ROAR # Mice SCRATCH, so we beat them with a ROAR
        elif opp == "Tiger" :
            return critter.POUNCE # Tigers ROAR, so we beat them with a POUNCE
        elif opp == "Elephant" :
            return critter.SCRATCH # Elephants POUNCE against non-tigers...
        else :
            print ("unknown opponent: ", opp )
            return None
        
        
        
