class Node(object):
    def __init__(self, label):
        self.label = label
        self.par = self
        self.size = 1
        self.sum = 0
        self.added = False


class DisjointSet(object):
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]

    def find(self, u):
        if u != u.par:  # here we user path compression trick
            u.par = self.find(u.par)
        return u.par

    def unite(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:  # u and v are in the same component
            return False

        # making v the vertex with bigger size
        if u.size > v.size:
            u, v = v, u

        # merging two components
        u.par = v

        # updating necessary variables
        v.size += u.size
        v.sum += u.sum

        return True


def solve(n, numbers, perm):
    # numbers is a list of n integers
    # perm is a list of the numbers 1 to n in some permutation
    # Return a list of answers
    #Implement the function
