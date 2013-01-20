import critter
import collections
import color
import inspect
import random
import os
import pprint

## TODO: GUI
## networking stuff? maybe later. pickle objects

# Just an (x, y) pair, but more readable.
Point = collections.namedtuple('Point', ['x', 'y'])

# Again, we don't really need a whole class just to store this info.
CritterInfo = collections.namedtuple('CritterInfo', ['x', 'y', 'width', 'height', 'getNeighbor'])

class CritterModel():
    """
    The main Critter simulation. Takes care of all the logic of Critter fights,
    and will eventually handle the GUI as well.
    """
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.critters = []
        self.move_count = 0
        # A map of critters to (x, y) positions.
        self.critter_positions = {}
        # A map of critter classes to the number alive of that class.
        self.critter_class_states = {}
        self.grid = [[None for x in range(height)] for x in range(width)]

    def add(self, critter, num):
        """
        Adds a particular critter type num times. The critter should be
        a class, not an instantiated critter.
        """
        if critter not in self.critter_class_states:
            self.critter_class_states[critter] = ClassInfo(initial_count=num)
        self.critter_class_states[critter].alive = num
        for i in range(num):
            args = CritterModel.create_parameters(critter)
            c = critter(*args)
            self.critters.append(c)
            pos = self.random_location()
            self.critter_positions[c] = pos
            self.grid[pos.x][pos.y] = c
    
    def update(self):
        """
        Takes care of updating all Critters. For each Critter, it firsts
        moves. If the position it moves to is occupied, the two critters
        fight, and the loser is destroyed while the winner moves into the
        position. Eventually, the GUI will be updated here.
        """
        self.move_count += 1
        random.shuffle(self.critters)
        # Unclean while loop, because we'll be removing any losing critters
        # as we iterate through the list.
        i = 0
        l = len(self.critters)
        while i < l:
            critter1 = self.critters[i]
            # Move the critter
            old_position = self.critter_positions[critter1]
            direction = critter1.getMove(CritterInfo(old_position.x, old_position.y,
                                                     self.width, self.height,
                                                     self.get_neighbor_func(old_position)))
            CritterModel.verify_move(direction)
            position = self.move(direction, old_position)
            # Fight, if necessary
            winner = critter1
            critter2 = self.grid[position.x][position.y]
            if critter2:
                winner = CritterModel.fight(critter1, critter2)
                loser = critter1 if winner == critter2 else critter2
                self.critter_positions[winner] = position
                # Get the loser out of here
                if loser in self.critter_positions:
                    index = self.critters.index(loser)
                    if index <= i:
                        i -= 1
                    self.critter_positions.pop(loser)
                    self.critters.remove(loser)
                    l -= 1
                else:
                    print("this shouldn't be happening!", i, l, self.critters)
                # Make sure we've got an accurate kill/alive count
                self.critter_class_states[loser.__class__].alive -= 1
                self.critter_class_states[winner.__class__].kills += 1
            self.grid[position.x][position.y] = winner
            self.grid[old_position.x][old_position.y] = None
            i += 1
        pprint.pprint(self.critter_class_states)
            
    def move(self, direction, pos):
        """
        Returns the new position after moving in direction. This assumes
        that (0, 0) is the top-left.
        """
        if direction == critter.NORTH:
            return Point(pos.x, (pos.y - 1) % self.height)
        elif direction == critter.SOUTH:
            return Point(pos.x, (pos.y + 1) % self.height)
        elif direction == critter.EAST:
            return Point((pos.x + 1) % self.width, pos.y)
        elif direction == critter.WEST:
            return Point((pos.x - 1) % self.width, pos.y)
        elif direction == critter.NORTHEAST:
            return Point((pos.x + 1) % self.width, (pos.y - 1) % self.height)
        elif direction == critter.NORTHWEST:
            return Point((pos.x - 1) % self.width, (pos.y - 1) % self.height)
        elif direction == critter.SOUTHWEST:
            return Point((pos.x + 1) % self.width, (pos.y + 1) % self.height)
        elif direction == critter.SOUTHEAST:
            return Point((pos.x - 1) % self.width, (pos.y - 1) % self.height)
        else:
            return pos
    
    def fight(critter1, critter2):
        """
        Force poor innocent Critters to fight to the death for the
        entertainment of Oberlin students. Returns the glorious victor.
        """
        weapon1 = critter1.fight(critter2.getChar())
        weapon2 = critter2.fight(critter1.getChar())
        CritterModel.verify_weapon(weapon1)
        CritterModel.verify_weapon(weapon2)
        if (weapon1 == critter.ROAR and weapon2 == critter.SCRATCH or
            weapon1 == critter.SCRATCH and weapon2 == critter.POUNCE or
            weapon1 == critter.POUNCE and weapon2 == critter.ROAR):
            critter1.fightOver(True, weapon2, critter2.getColor())
            critter2.fightOver(False, weapon1, critter1.getColor())
            return critter1
        elif weapon1 == weapon2:
            if random.random() > .5:
                critter1.fightOver(True, weapon2, critter2.getColor())
                critter2.fightOver(False, weapon1, critter1.getColor())
                return critter1
            else:
                critter1.fightOver(False, weapon2, critter2.getColor())
                critter2.fightOver(True, weapon1, critter1.getColor())
                return critter2
        else:
                critter1.fightOver(False, weapon2, critter2.getColor())
                critter2.fightOver(True, weapon1, critter1.getColor())
                return critter2

    def verify_weapon(weapon):
        "Make sure students are using the right weapons. If not, throws an exception."
        if weapon not in (critter.ROAR, critter.POUNCE, critter.SCRATCH):
            raise WeaponException("Critter weapon must be ROAR, POUNCE, or SCRATCH!")
    
    def verify_move(move):
        "Make sure they don't move diagonally."
        if move not in (critter.NORTH, critter.SOUTH, critter.EAST, critter.WEST, critter.CENTER):
            raise LocationException("Don't move diagonally! %s" % move)

    def verify_location(location):
        "Make sure students are using the right locations. If not, throws an exception."
        if location not in (critter.NORTH, critter.NORTHEAST, critter.NORTHWEST,
                            critter.SOUTH, critter.SOUTHEAST, critter.SOUTHWEST,
                            critter.EAST, critter.WEST, critter.CENTER):
            raise LocationException("That is not a real direction!")

    def random_location(self):
        """
        Calculate a random location for a Critter to be placed. This is not
        guaranteed to terminate by any means, but practically we (probably)
        don't need to be concerned.

        Returns a 2-tuple of integers.
        """
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        while self.grid[x][y] is not None:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
        return Point(x, y)
    
    def create_parameters(critter):
        """
        This is a bit funky. Because not all Critters take the same
        arguments in their constructor (for example, a Mouse gets a
        color while an Elephant gets an int), we need to check the
        classname and return appropriate things based on that. The
        Java version is a bit nicer because it has access to type
        information for each parameter, but c'est la vie.
        
        Return value is a tuple, which will be passed as *args to
        the critter's constructor.
        """
        if critter.__name__ == 'Mouse':
            return (color.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),)
        elif critter.__name__ == 'Elephant':
            return (random.randint(1, 15),)
        # No other class needs parameters
        else:
            return ()
    
    def get_neighbor_func(self, position):
        "Returns the getNeighbor function for a particular position."
        def get_neighbor(direction):
            neighbor_pos = self.move(direction, position)
            neighbor = self.grid[neighbor_pos.x][neighbor_pos.y]
            return neighbor.getChar() if neighbor else '.'
        return get_neighbor

    def results(self):
        """
        Returns the critters in the simulation, sorted by alive+kills.
        results()[0] is (overall winner, state of winner).
        """
        return sorted(self.critter_class_states.items(),
                      key=lambda state: state[1].kills + state[1].alive)
        
            
class ClassInfo():
    """
    This would be a named tuple, but they're immutable and that's somewhat
    unwieldy for this particular case.
    """
    def __init__(self, kills=0, alive=0, initial_count=0):
        self.kills = kills
        self.alive = alive
        self.count = initial_count
    
    def __repr__(self):
        return '%s %s %s' % (self.kills, self.alive, self.count)

# These exceptions don't really need fancy names
class WeaponException(Exception):
    pass

class LocationException(Exception):
    pass

if __name__ == '__main__':
    critters = get_critters()
    print(critters)
