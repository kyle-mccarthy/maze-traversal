from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertices = list()
        self.start = None
        self.end = None
        self.shortest_path = list()

    ## Read the matrix into a graph and store the available moves as vertices
    def read_matrix_to_graph(self, file_matrix):
        row = 0
        col = 0
        # row
        for r in file_matrix:
            # column
            for c in r:
                # handle the matrix spots, if it isn't an expected input
                # treat it like a wall
                if c == " " or c == "S" or c == "E":
                    v = Vertex()
                    v.col = col
                    v.row = row
                    # start node
                    if c == "S":
                        v.start = True
                        self.start = v
                    # end node
                    if c == "E":
                        v.end = True
                        self.end = v
                    self.vertices.append(v)
                col += 1
            col = 0
            row += 1

    # find adjacent vertices for each vertex
    #   0 1 2 3
    # 0 # # . #
    # 1 # . V .
    # 2 # # . #
    # 3 # # # #
    def find_adjacent(self):
        for v in self.vertices:
            for adj in self.vertices:
                if (v.col == adj.col and v.row - 1 == adj.row or     # N
                    v.col + 1 == adj.col and v.row == adj.row or     # E
                    v.col == adj.col and v.row + 1 == adj.row or     # S
                        v.col - 1 == adj.col and v.row == adj.row):  # W
                    v.adj.append(adj)

    # print the adjacency list for the graph
    def print_adj_list(self):
        for v in self.vertices:
            print "(", v.row, ",", v.col, "): ",
            for adj in v.adj:
                print "(", adj.row, ",", adj.col, ") ",
            print

    # perform a BFS on the graph using the adjacency list
    def bfs(self):
        q = list()
        q.append([self.start])
        while q:
            path = q.pop(0)
            v = path[-1]
            # end of maze
            if v is self.end:
                self.shortest_path = path
                return path
            # enqueue the adjacent nodes
            elif v.visited is False:
                for adj in v.adj:
                    new_path = list(path)
                    new_path.append(adj)
                    q.append(new_path)
                v.visited = True

    # perform DFS on the graph and set the successors
    def dfs(self, v):
        if v.successor is None:
            v.cost = 0
        v.visited = True
        for adj in v.adj:
            if adj.visited is False:
                # set the parent
                adj.successor = v
                adj.cost = v.cost + 1
                self.dfs(adj)
            # if the cost is less switch the successor
            # and set the new cost
            if adj.cost > v.cost + 1:
                adj.successor = v
                adj.cost = v.cost + 1
                self.dfs(adj)

    # build the shortest path based on the end to start successors
    def calc_shortest_path(self, v):
        if v.successor is None:
            self.shortest_path.reverse()
            return
        self.shortest_path.append(v)
        self.calc_shortest_path(v.successor)

    def print_shortest_path(self):
        for v in self.shortest_path:
            print "(", v.row, ", ", v.col, ") ",
