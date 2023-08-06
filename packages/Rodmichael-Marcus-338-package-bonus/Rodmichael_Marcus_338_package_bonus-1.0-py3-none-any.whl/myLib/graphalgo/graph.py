class graph():
    def __init__(self, order: int = 0, size: int = 0):
        self.order = order
        self.size = size
        self.graph_structure = [[] for element in range(order)]

    def add_vertex(self):
        pass

    def add_edge(self, source: int, destination: int, weight: float = 1.0):
        pass
