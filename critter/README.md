# Critters!
## The critter lab, Python-style.

There are a lot more files in this version than in the old one.

* <critter>.py -- This should be pretty obvious.
* color.py -- This defines a color object (a triple of r, g, b), and some constants for commonly-used colors.
* critter_model.py -- The critter simulation itself. This doesn't handle any of the GUI or user interface stuff, just the fighting/moving/etc.
* critter_gui.py -- Handles all the drawing and stuff. Depends solely on a CritterModel object.
* critter_main.py -- The main function, etc. Finds all the critter classes and instantiates them in a CritterModel, and (depending on the command-line args) either does a quick fight with no GUI, or shows the fight for the in-class tournament.

## Usage
    $> ./critter_main.py --fight BenK BobG
will run the GUI, fighting Ben and Bob's critters along with the standard Tiger, Mouse, etc.
    $> ./critter_main.py --quickfight BenK BobG
will do the same thing, but no GUI. A list of the results is printed at the end.