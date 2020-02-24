from test_helper import *
from task import solve
import string, random


class Node(object):
    def __init__(self, label):
        self.label = label
        self.par = self
        self.rank = 0
        self.min = 0


class DisjointSet(object):
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]

    def find(self, u):
        if u == u.par:
            return u
        return self.find(u.par)

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:  # u and v are in the same component
            return False

        # making v the vertex with better rank
        if u.rank > v.rank:
            u, v = v, u

        # merging two components
        u.par = v

        # updating maximum depth as rank
        if u.rank == v.rank:
            v.rank += 1

        v.min = min(v.min, u.min)

        return True

    # Returns a list of components where each component is a list of values
    def get_all_components(self):
        comps = [[] for _ in range(self.n)]
        for node in self.nodes:
            comps[self.find(node).label].append(node.label)

        comps = [i for i in comps if i]  # Remove empty lists
        return comps


def solve2(n, m, words, prices, groups, message):
    dsu = DisjointSet(n)
    indices = {}
    for i in range(n):
        dsu.nodes[i].min = prices[i]
        indices[words[i]] = i

    for group in groups:
        for i in range(len(group)):
            dsu.union(dsu.nodes[group[0]], dsu.nodes[group[i]])

    price = 0
    for word in message:
        price += dsu.find(dsu.nodes[indices[word]]).min

    return price


def string_generator(size, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def partition(lst, n):
    random.shuffle(lst)
    division = len(lst) / float(n)
    return [lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n)]


if __name__ == '__main__':
    manual_tests = [
        (5, 4, ['i', 'loser', 'am', 'the', 'second'], [100, 1, 1, 5, 10], [[0], [2], [1, 4], [3]],
         ['i', 'am', 'the', 'second'], 107),

        (5, 4, ['i', 'loser', 'am', 'the', 'second'], [100, 20, 1, 5, 10], [[0], [2], [1, 4], [3]],
         ['i', 'am', 'the', 'second'], 116),

        (1, 1, ['a'], [1000000000], [[0]], ['a'], 1000000000),

        (1, 10, ['a'], [1000000000], [[0]], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 10000000000),
    ]

    for test in manual_tests:
        n, m, words, prices, groups, message, ans1 = test
        ans2 = solve(n, m, words, prices, groups, message)
        if ans1 != ans2:
            failed("Wrong Answer! Input: {}, your output: {}, answer: {}".format((words, prices, groups, message), ans2,
                                                                                 ans1))

        random_tests = 10
        for i in range(random_tests):
            n = random.randint(1000, 10000)
            m = random.randint(1000, 10000)
            k = random.randint(1, min(10, n))
            words = [string_generator(random.randint(10, 20)) for _ in range(n)]
            prices = [random.randint(1, 10000) for _ in range(n)]
            lst = [i for i in range(n)]
            groups = partition(lst, k)
            message = [words[random.randint(0, n - 1)] for _ in range(m)]
            ans2 = solve(n, m, words, prices, groups, message)
            ans1 = solve2(n, m, words, prices, groups, message)
            if ans2 != ans1:
                failed("Wrong Answer! Input: {}, your output: {}, answer: {}".format((words, prices, groups, message),
                                                                                     ans2,
                                                                                     ans1))
