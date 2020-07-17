from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
def print_room_and_exits():
    pass
    print(f" - ROOM - : {player.current_room.id}, - EXITS - : {player.current_room.get_exits()}")

# takes in a direction string, and returns the opposite direction as a string
def get_opposite_direction(direction):
    if direction == "n":
        return "s"
    if direction == "s":
        return "n"
    if direction == "w":
        return "e"
    if direction == "e":
        return "w"

# takes in a list of directions, returns a random one
def pick_random_direction(exits):
    index = random.randint(0, len(exits) - 1)
    print(f"Exits len = {len(exits)}, 0-{len(exits) - 1}, picked index {index}, final = {exits[index]}")
    return exits[index]

# move in this direction and then print out room and exits
def traverse(rand_dir):
    player.travel(rand_dir, True)
    print_room_and_exits()

# from Player class
# def travel(self, direction, show_rooms = False):
#         next_room = self.current_room.get_room_in_direction(direction)
#         if next_room is not None:
#             self.current_room = next_room
#             if (show_rooms):
#                 next_room.print_room_description(self)
#         else:
#             print("You cannot move in that direction.")

# # From Graph, replace starting_vertex with current room
# def dft(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """
#         print("DFT called (pt 3)")

#         # make a stack
#         stack = Stack()

#         # push on our starting node
#         stack.push(starting_vertex)

#         # make a Set to track if we've been here before
#         visited = set()

#         # while our stack isn't empty
#         while stack.size() > 0:

#             # pop off whatever's on top, this is current_node
#             current_node = stack.pop()

#             # if we haven't visited this vertex before
#             if current_node not in visited:

#                 # mark as visited
#                 visited.add(current_node)

#                 # print it
#                 print(f"current_node = {current_node}")

#                 # get its neighbors
#                 neighbors = self.get_neighbors(current_node)

#                 #for each of the neighbors  
#                 for neighbor in neighbors:
#                     # add to the Stack
#                     stack.push(neighbor)

# do main work here
def search_all_rooms():

    # list of directions to take that is returned at the end
    path = []

    # keeps while loop going
    stack = Stack()

    # Rooms visited. Key = id, Value = [exits: id] ?
    visited = {}
    visited_count = 0

    # key is room id, value is exits that aren't explored
    paths_to_explore = {}

    # 1. Start at Room 0
    print_room_and_exits()

    test = player.current_room.get_room_in_direction("n")
    print(f"test = {test.id}")

    # paths_to_explore[player.current_room.id] = player.current_room.get_exits()

    # 1.2. Head north to start off
    # traverse("n")

    # add to visited
    # visited[player.current_room.id] = dict()
    # path.append("n")
    # neighbors = player.current_room.get_exits()
    # paths_to_explore[player.current_room.id] = []
    # for room in neighbors:
    #     print(f"room = {room}")
    #     # not done with this?
    #     visited[player.current_room.id][room] = "?"
    #     paths_to_explore[player.current_room.id].append(room)
    # set last room
    last_room = 0

    # set last direction
    last_direction = "end"

    # back track (for when you hit a dead end)
    back_track_path = Stack()

    
    stack.push(player.current_room.id)
    # neighbors = player.current_room.get_exits()
        # paths_to_explore[player.current_room.id] = [] # ?
    #     last_direction = "end" 
    #     for room in neighbors:
    #         print(f"room = {room}")
    #         # check which rooms have been explored already
    #         # rand_dir = pick_random_direction(neighbors)
            
    #         if player.current_room.get_room_in_direction(room).id not in visited:
    #             last_direction = room

    # print(f"paths to explore = {paths_to_explore}")
    exits = []

    total_rooms = len(room_graph)
    while True:

        if visited_count == total_rooms:
            print("all rooms visited, breaking")
            break

        # # add to visited and increment count
        # if player.current_room.id not in visited:
        #     visited[player.current_room.id] = dict()
        #     visited_count += 1
        # # else:
        
        # possible exits for current room
        # exits = paths_to_explore[player.current_room.id]
        if last_direction == "end":
            # dead end
            print("Dead End")
            print(f"last_direction = {last_direction}")
            last_direction = back_track_path.pop()
            path.append(last_direction)
            traverse(last_direction)
        else:
            # pick random direction
            # rand_dir = pick_random_direction(exits)
            # print(f"random direction: {rand_dir}")
            
            path.append(last_direction)
            back_track_path.push(get_opposite_direction(last_direction))
            traverse(last_direction)

            # add to visited
            visited[player.current_room.id] = dict()
            exits = player.current_room.get_exits()
            for exit in exits:
                visited[player.current_room.id][exit] = player.current_room.get_room_in_direction(exit).id
            visited_count += 1

            print(f"visited[{player.current_room.id}]: {visited[player.current_room.id]}")
            print(f"{player.current_room.id}: {visited[player.current_room.id]}")
            print(f"last direction = {last_direction}")


        neighbors = player.current_room.get_exits()
        # paths_to_explore[player.current_room.id] = []
        last_direction = "end"
        # for each neighbor
        for room in neighbors:
            print(f"room = {room}")
            # check which rooms have been explored already
            # rand_dir = pick_random_direction(neighbors)
            
            if player.current_room.get_room_in_direction(room).id not in visited:
                last_direction = room
        
    print(f"visited = {visited}")
    print(f"paths to explore = {paths_to_explore}")
            
    return path

# search_all_rooms should return a list of directions to follow
print(f"EXITS: {player.current_room.get_exits()}")
print(f"ID: {player.current_room.id}")
print("Now giving directions to traversal path")
print(f"world.grid_size = {world.grid_size}")
print(f"total num of rooms: {len(room_graph)}")
traversal_path = search_all_rooms()


# DONT TOUCH THIS
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
