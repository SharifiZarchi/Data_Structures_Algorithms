class DisjointSet(object):
    def __init__(self, n):
        self.n = n
        # list of components of each set
        self.set_lists = [[i] for i in range(n)]
        # pointing to the set of each component
        self.set = [i for i in range(n)]

    def find(self, u):
        return self.set[u]

    def unite(self, u, v):
        u_set, v_set = self.find(u), self.find(v)
        if u_set == v_set:  # u and v are in the same component
            return False

        # set u to the smaller list
        if len(self.set_lists[u_set]) > len(self.set_lists[v_set]):
            u_set, v_set = v_set, u_set

        # merging the smaller list into the large list
        for i in self.set_lists[u_set]:
            self.set_lists[v_set].append(i)
            # updating set of each element
            self.set[i] = v_set

        return True

    def get_count(self):
        count = 0
        for i in range(self.n):
            if self.set[i] == i:
                count += 1
        return count


def solve(n, points):
    assert len(points) == n
    #Implement the function

