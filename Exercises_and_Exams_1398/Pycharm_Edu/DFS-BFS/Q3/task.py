from collections import defaultdict

class graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)
        self.eSize = 0

    def addEdge(self,u,x):
        self.graph[u].append(x)
        self.graph[x].append(u)
        self.eSize += 1

def maxDistance(g):
return 0 #Implement the function

