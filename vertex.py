class Vertex:
    def __init__(self):
        self.row = None
        self.col = None
        self.adj = []  # for BFS
        self.visited = False  # for BFS
        self.start = False
        self.end = False
        self.successor = None
        self.cost = None

    # add an adjacent edge
    def add_adjacent(self, v):
        self.adj.append(v)