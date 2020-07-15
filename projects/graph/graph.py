"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    # Part 1. DONE
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        result = "\n"
        for vertex in self.vertices:
            result += f"{vertex}: {self.vertices[vertex]}"
            result += "\n"
        return result

    # Part 1. DONE
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        
    # Part 1. DONE
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)
        # do opposite too if undirected graph
        # self.vertices[v2].add(v1)

    # Part 1. DONE
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id] # return its value (set)

    # Part 2. DONE
    # data structure for BFT: Queue
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print("BFT called (pt 2)")
        # make a Queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # make a Set to track if we've been here before
        visited = set()
        # while our Queue isn't empty, we will dequeue whatevers at the front of the line
        while q.size() > 0:

            # dequeue whatevers at the front of the line, this is our current_node
            current_node = q.dequeue()
            
            # if we haven't visited this node yet
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
                # print it
                print(f"current_node = {current_node}")
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors
                for neighbor in neighbors:
                    # add to the Queue
                    q.enqueue(neighbor)

    # Part 3. DONE?
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print("DFT called (pt 3)")

        # make a stack
        stack = Stack()

        # push on our starting node
        stack.push(starting_vertex)

        # make a Set to track if we've been here before
        visited = set()

        # while our stack isn't empty
        while stack.size() > 0:

            # pop off whatever's on top, this is current_node
            current_node = stack.pop()

            # if we haven't visited this vertex before
            if current_node not in visited:

                # mark as visited
                visited.add(current_node)

                # print it
                print(f"current_node = {current_node}")

                # get its neighbors
                neighbors = self.get_neighbors(current_node)

                #for each of the neighbors  
                for neighbor in neighbors:
                    # add to the Stack
                    stack.push(neighbor)

    # Part 4. DONE?
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print("DFT Recursive called (pt 4)")
        
        # mark this vertex as visited
        visited.add(starting_vertex)
        print(f"starting = {starting_vertex}")
        # if len(neighbors) == 0: then return 

        # for each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            # if its not visited
            if neighbor not in visited:
                #recursive on the neighbor
                self.dft_recursive(neighbor, visited)

        # redundant
        return None

    # Part 5.
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print("BFS called (pt 5)")

        # solution version
        # make a queue
        q = Queue()

        # make a set to track nodes we've visited
        visited = set()

        # NEW
        path = [starting_vertex]
        q.enqueue(path)

        # while queue isn't empty
        while q.size() > 0:

            ## dequeue the node at the front of the line
            current_path = q.dequeue()
            current_node = current_path[-1]

            ### if this node is our target node
            if current_node == destination_vertex:
                #### return it. return true
                return current_path

            ### if NOT visited
            if current_node not in visited:
                #### mark as visited
                visited.add(current_node)

                #### get its neighbors
                neighbors = self.get_neighbors(current_node)

                #### for each neighbor
                for neighbor in neighbors:
                    ##### add to our queue
                    # copy path so we don't mutate the original path for different
                    # current_path.append(neighbor)
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    
                    q.enqueue(path_copy)


        # # My version
        # # make a Queue
        # q = Queue()
        # # enqueue our starting node
        # q.enqueue(starting_vertex)
        # # make a Set to track if we've been here before
        # visited = set()
        # # while our Queue isn't empty, we will dequeue whatevers at the front of the line
        # while q.size() > 0:

        #     # dequeue whatevers at the front of the line, this is our current_node
        #     current_node = q.dequeue()
            
        #     # if we haven't visited this node yet
        #     if current_node not in visited:
        #         # mark as visited
        #         visited.add(current_node)
        #         # print it
        #         print(f"current_node = {current_node}")

        #         if current_node == destination_vertex:
        #             print(f"current_node == destination_vertex {destination_vertex}")
        #             print("heres the current queue")
        #             result = []
        #             # for node in visited:
        #             #     # result.append(node)
        #             # print(f"result list = {result}")
        #         # get its neighbors
        #         neighbors = self.get_neighbors(current_node)
        #         # for each of the neighbors
        #         for neighbor in neighbors:
        #             # add to the Queue
        #             q.enqueue(neighbor)

    # Part 6.
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print("DFS called (pt 6)")

        # make a stack
        stack = Stack()

        # push on our starting node
        stack.push(starting_vertex)

        # make a Set to track if we've been here before
        visited = set()

        # while our stack isn't empty
        while stack.size() > 0:

            # pop off whatever's on top, this is current_node
            current_node = stack.pop()

            # if we haven't visited this vertex before
            if current_node not in visited:

                # mark as visited
                visited.add(current_node)

                # print it
                print(f"current_node = {current_node}")

                # get its neighbors
                neighbors = self.get_neighbors(current_node)

                # check to see if any neighbors happen to be the destination vertex 
                for neighbor in neighbors:
                    print(f"neighbor = {neighbor}")
                    if neighbor == destination_vertex:
                        print(f"found in neighbors, visited = {visited}")
                        resultList = []
                        for node in visited:
                            resultList.append(node)
                        resultList.append(neighbor)
                        print(f"resultList = {resultList}")
                        return resultList

                #for each of the neighbors  
                for neighbor in neighbors:

                    if neighbor == destination_vertex:
                        print(f"found in neighbors, visited = {visited}")
                        print(visited)
                    # add to the Stack
                    stack.push(neighbor)
    
    # Part 7.
    def dfs_recursive(self, vertex, destination_vertex, path=[], visited= set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print("DFS Recursive called (pt 7)")
        
        # mark our node as visited
        visited.add(vertex)

        # check if its our target node, if so return
        if vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(vertex)

        # iterate over neighbors
        neighbors = self.get_neighbors(vertex)

        # check if visited
        for neighbor in neighbors:
            if neighbor not in visited:
                # if not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)

                # if this recursion returns a path
                if result is not None:
                    return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph) # used to be graph.vertices
    
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

# Solving Graph Problems
# 1. Describe the problem using graphs terminology
# 2. Build your graph, or write your getNeighbors()
# 3. Choose your algorithm, and apply it

# Given two words

# Word Ladder Problem (needs words file imported)

# from util import Queue
# import string
# ​
# # Build our graph
# ## Could filter our word list by length
# ## remember to lower case stuff
# ​
# # filtered_word_list = filter()
# # for word1 in word_list:
# #     for word2 in word_list:
# #         if one_letter_off(word1, word2):
# #             Graph.add_edge
# ​
# # len(word) * 26
# # O(n * 26)
# # O(26n)
# # O(n)
# my_file = open('words.txt', 'r')
# words = my_file.read().split("\n")
# my_file.close()
# ​
# word_set = set()
# for word in words:
#     word_set.add(word.lower())
# ​
# def get_neighbors(start_word):
#     neighbors = []
# # for every letter in the word,
#     for letter_index in range(len(start_word)):
#         # for every letter in the alphabet
#         for letter in string.ascii_lowercase:
# ​
#             ## turn our start word into a list, then back again
#             word_list = list(start_word)
#         ## swap out a letter in the alphabet
#             word_list[letter_index] = letter
# ​
#             word = "".join(word_list)
# ​
#         ### if the result is in our words list, it's a neighbor!
#             if word in word_set and word != start_word:
#                 neighbors.append(word)
# ​
#     return neighbors
# ​
# ​
# # BFS
# def word_ladders(start_word, end_word):
#    q = Queue() 
# ​
#    visited = set()
# ​
#    q.enqueue([start_word])
# ​
#    while q.size() > 0:
# ​
#        current_path = q.dequeue()
#        current_word = current_path[-1]
# ​
#        if current_word == end_word:
#            return current_path
# ​
#        if current_word not in visited:
#            visited.add(current_word)
# ​
#            neighbors = get_neighbors(current_word)
# ​
#            for neighbor in neighbors:
#                path_copy = list(current_path)
#                path_copy.append(neighbor)
#                q.enqueue(path_copy)
# ​
# print(word_ladders('sail', 'boat'))