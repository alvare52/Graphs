
# Islands Matrix Problem
# Write a function that takes a 2D binary array and returns the number of 1 islands. 
# An island consists of 1s that are connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

# Nodes: 1's
# Edges: Connected N/S/W/E
# Islands: Connected Components

# Build our graph or just define getNeighbors()