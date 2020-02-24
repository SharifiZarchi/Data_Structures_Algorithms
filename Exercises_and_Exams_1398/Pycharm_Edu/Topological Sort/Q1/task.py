import copy


class Graph:
    def __init__(self, N):
        self.graph = [[] for _ in range(N)]
        self.Vertices_num = N
        self.result = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def all_topologicals(self):
        return -1 #Implement the function

    


# Don't change this function
def solve(graph):
    return graph.all_topologicals()


