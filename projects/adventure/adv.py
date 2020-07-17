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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
    print(f"* Room {player.current_room.id}, Exits: {player.current_room.get_exits()} *")

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

# do main work here
def search_all_rooms():

    # list of directions to take that is returned at the end
    path = []

    # keeps while loop going
    stack = Stack()

    # Rooms visited. Key = id, Value = [exits] ?
    visited = {}
    visited_count = 0

    # keep track of the room we came from and direction
    last_room = None
    last_direction = ""

    # keep track of how to get back to last fork
    back_track_path = []

    #
    paths_to_explore = {}

    # 1. Start at Room 0
    print_room_and_exits()
    stack.push(player.current_room.id)

    while stack.size() > 0:

        if visited_count == len(room_graph):
            print("all rooms visited, breaking")
            break

        current = stack.pop()
        last_room = current
        

        # print(f"current = {current}")
        # if we are in a room we have NOT visited yet, add it to visited
        if current not in visited:
            # add to visited
            visited[current] = dict()
            visited_count += 1
            # add key (id) and value (dict of exits, where key is direction and value is id)
            # then, get this room's exits and add them to the value of visited[current] value dict
            neighbors = player.current_room.get_exits()
            paths_to_explore[current] = []
            for room in neighbors:
                # print(f"room = {room}")
                # not done with this?
                visited[current][room] = "?"
                paths_to_explore[current].append(room)

        # print(f"paths_to_explore for {current} = {paths_to_explore[current]}")
        # print(f"visited: {visited}")

        # 2. Check exits [n, s, w, e] (pick randomint from 1-4, n=1,s=2,etc...)
        rand_dir = pick_random_direction(player.current_room.get_exits())
        # print(f"random direction: {rand_dir}")

        # add direction we will go in to the path
        path.append(rand_dir)
        # print(f"path now: {path}")

        # 4. Take random exit that has NOT been visited ?
        last_direction = rand_dir
        traverse(rand_dir)
        stack.push(player.current_room.id)
        # now we can add the exits value opposite key to the last room id we were in
    
    # print(f"last room = {last_room}")
            
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
