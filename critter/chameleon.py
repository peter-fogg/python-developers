import critter
import color

class Chameleon(critter.Critter):
    
    num_scratch = 0
    num_roar = 0
    num_pounce = 0
    num_wins = 0
    
    def __init__(self):
        self.color = color.GREEN
        self.char = 'C'
    
    def fight(self, oppInfo):
        self.color = oppInfo.color
        strategy = max(Chameleon.num_scratch, Chameleon.num_roar, Chameleon.num_pounce)
        if strategy == critter.SCRATCH:
            return critter.ROAR
        elif strategy == critter.ROAR:
            return critter.POUNCE
        return critter.SCRATCH

    def getColor(self):
        return self.color

    def getMove(self, info):
        if Chameleon.num_wins < 0:
            if info.getNeighbor(critter.NORTH) == '.':
                return critter.NORTH
            if info.getNeighbor(critter.SOUTH) == '.':
                return critter.SOUTH
            if info.getNeighbor(critter.EAST) == '.':
                return critter.EAST
            if info.getNeighbor(critter.WEST) == '.':
                return critter.WEST
            else:
                return critter.CENTER
        if info.getNeighbor(critter.NORTH) != '.':
            return critter.NORTH
        if info.getNeighbor(critter.SOUTH) != '.':
            return critter.SOUTH
        if info.getNeighbor(critter.EAST) != '.':
            return critter.EAST
        else:
            return critter.WEST
    
    def getChar(self):
        return self.char
    
    def fightOver(self, won, oppFight ):
        if won:
            Chameleon.num_wins += 1
        else:
            Chameleon.num_wins -= 1
        if oppFight == critter.SCRATCH:
            Chameleon.num_scratch += 1
        elif oppFight == critter.ROAR:
            Chameleon.num_roar += 1
        else:
            Chameleon.num_pounce += 1
