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

    # Part 3.
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

    # Part 4.
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print("DFT Recursive called (pt 4)")
        pass  # TODO

    # Part 5.
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print("BFS called (pt 5)")
        pass  # TODO

    # Part 6.
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print("DFS called (pt 6)")
        pass  # TODO
    
    # Part 7.
    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print("DFS Recursive called (pt 7)")
        pass  # TODO

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
