#!/usr/bin/env python3
import inspect
import os

# Constants for movement.
NORTH = -2
NORTHEAST = 27
NORTHWEST = 102
SOUTH = 4
SOUTHEAST = 99
SOUTHWEST = -31
EAST = 3
WEST = 19
CENTER = 11

# Constants for attack
ROAR = 28
POUNCE = -10
SCRATCH = 55
    
class Critter():
    """
    The base Critter class.
    """

    # I'm not sure what the default behavior for this should be.
    def __init__(self):
        pass
        
    # @param opponent The character of the current opponent.
    # @returns Your attack: ROAR, POUNCE, or SCRATCH
    def fight(self, opponent):
        pass
    
    # Give your color.
    # @returns Your current color.
    def getColor(self):
        pass
    
    # Give your direction.
    # @returns A cardinal direction, in the form of a constant (NORTH, SOUTH)
    def getMove(self, info):
        pass
    
    # Give your character.
    # @returns Whichever character represents this critter.
    def getChar(self):
        pass
    
    # End of fight shenanigans.
    # @param won Boolean; true if won fight, false otherwise.
    # @param oppMove Opponent's movement (ROAR, etc)
    # @param oppColor Opponent's color.
    # @returns Nothing.
    def fightOver(self, won, oppMove, oppColor):
        pass
