# Necessary modules:
-pygame
-numpy

# How it works?
Run the program by opening and running main.py, file sand.py contains Grid class, which creates a 2D grid with a given number of divisions.

By clicking anywhere in the window, user "creates" sand -> grid value at that point changes from 0 to 1. If there is nothing underneath the sand particle, particle falls down, however if sand is present under and the particle cannot fall further, sand is "dispersed"t to either side.


