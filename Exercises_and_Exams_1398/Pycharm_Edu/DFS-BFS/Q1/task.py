from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,v,w):
        self.graph[v].append(w)
        self.graph[w].append(v)





def hasCycle(g):
    #Implement the function