#!/usr/bin/env python3

'''
Script for facilitating the Critter tournament.
'''

import os
import shutil
import sys

WINNERS = './winners/'
LOSERS = './losers/'
WAITING = './waiting/'

def setup():
    'Sets up the directories for the tournament, if necessary.'
    directories = filter(lambda x: not os.path.exists(x), [WINNERS, LOSERS, WAITING])
    for directory in directories:
        os.mkdir(directory)

def startfight():
    'Moves the next two critters into the current directory. '
    critters = os.listdir(WAITING)
    if len(critters) == 2 and os.listdir(WINNERS) == []:
        print('Final round: %s and %s' % (critters[0], critters[1]))
        shutil.move(WAITING + critters[0], './' + critters[0])
        shutil.move(WAITING + critters[1], './' + critters[1])
    elif len(critters) < 2:
        print('No more critters to fight, starting next round')
        for critter in os.listdir(WINNERS):
            shutil.move(WINNERS + critter, WAITING + critter)
    else:
        print('Next up: %s and %s' % (critters[0], critters[1]))
        shutil.move(WAITING + critters[0], './' + critters[0])
        shutil.move(WAITING + critters[1], './' + critters[1])

def fightover(winner, loser):
    'Moves the winner into the winners directory, similarly for the loser.'
    shutil.move('./' + winner, WINNERS + winner)
    shutil.move('./' + loser, LOSERS + loser)

def main():
    if len(sys.argv) == 1:
        print('What to do?')
        sys.exit(1)
    elif sys.argv[1] == 'setup':
        setup()
    elif sys.argv[1] == 'startfight':
        startfight()
    elif sys.argv[1] == 'fightover' and len(sys.argv) >= 4:
        fightover(sys.argv[2], sys.argv[3])
    else:
        print("That doesn't make sense.")

if __name__ == '__main__':
    main()
