from test_helper import *
from task import solve
import random
import string


class Node(object):
    def __init__(self, label):
        self.label = label
        self.par = self
        self.rank = 0


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

        return True

    # Returns a list of components where each component is a list of values
    def get_all_components(self):
        comps = [[] for _ in range(self.n)]
        for node in self.nodes:
            comps[self.find(node).label].append(node.label)

        comps = [i for i in comps if i]  # Remove empty lists
        return comps


def solve2(n, a, b):
    dsu = DisjointSet(26)
    for i in range(n):
        n1 = dsu.nodes[ord(a[i]) - ord('a')]
        n2 = dsu.nodes[ord(b[i]) - ord('a')]
        dsu.union(n1, n2)
    comps = dsu.get_all_components()

    ans = 26 - len(comps)
    rules = []
    for i in comps:
        if len(i) > 1:
            for j in range(1, len(i)):
                rules.append((chr(ord('a') + i[0]), chr(ord('a') + i[j])))

    return ans, rules


def check_answer(n, a, b, ans, rules):
    dsu1 = DisjointSet(26)
    for i in range(n):
        n1 = dsu1.nodes[ord(a[i]) - ord('a')]
        n2 = dsu1.nodes[ord(b[i]) - ord('a')]
        dsu1.union(n1, n2)

    dsu2 = DisjointSet(26)
    for rule in rules:
        c1, c2 = rule
        c1 = dsu2.nodes[ord(c1) - ord('a')]
        c2 = dsu2.nodes[ord(c2) - ord('a')]
        dsu2.union(c1, c2)

    for i in range(26):
        dsu1.find(dsu1.nodes[i])
        dsu2.find(dsu1.nodes[i])
    for i in range(26):
        label2 = dsu2.find(dsu2.nodes[i]).label
        n1 = dsu1.find(dsu1.nodes[label2]).label
        n2 = dsu1.find(dsu1.nodes[i]).label
        if n1 != n2:
            failed("Wrong Answer! Input: {}, your output: {}, answer: {}".format((n, a, b), (ans, rules),
                                                                                 solve2(n, a, b)))


def string_generator(size, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    manual_tests = [
        (3, 'abb', 'dad'),
        (8, 'drpepper', 'cocacola'),
        (1, 'h', 'p'),
        (2, 'cx', 'da'),
        (3, 'bab', 'aab'),
        (15, 'xrezbaoiksvhuww', 'dcgcjrkafntbpbl'),
        (10, 'daefcecfae', 'ccdaceefca'),
        (10, 'fdfbffedbc', 'cfcdddfbed'),
        (100, 'bltlukvrharrgytdxnbjailgafwdmeowqvwwsadryzquqzvfhjnpkwvgpwvohvjwzafcxqmisgyyuidvvjqljqshflzywmcccksk',
         'jmgilzxkrvntkvqpsemrmyrasfqrofkwjwfznctwrmegghlhbbomjlojyapmrpkowqhsvwmrccfbnictnntjevynqilptaoharqv'),

        (100, 'pfkskdknmbxxslokqdliigxyvntsmaziljamlflwllvbhqnzpyvvzirhhhglsskiuogfoytcxjmospipybckwmkjhnfjddweyqqi',
         'akvzmboxlcfwccaoknrzrhvqcdqkqnywstmxinqbkftnbjmahrvexoipikkqfjjmasnxofhklxappvufpsyujdtrpjeejhznoeai'),

        (3, 'whw', 'uuh'),
        (242,
         'rrrrrrrrrrrrrmmmmmmmmmmmmmgggggggggggggwwwwwwwwwwwwwyyyyyyyyyyyyyhhhhhhhhhhhhhoooooooooooooqqqqqqqqqqqqqjjjjjjjjjjjjjvvvvvvvvvvvvvlllllllllllllnnnnnnnnnnnnnfffffffffffffeeeeeeeeaaaaaaaaiiiiiiiiuuuuuuuuzzzzzzzzbbbbbbbbxxxxxxxxttttttttsscckppdd',
         'rmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfrmgwyhoqjvlnfeaiuzbxteaiuzbxteaiuzbxteaiuzbxteaiuzbxteaiuzbxteaiuzbxteaiuzbxtscsckpdpd')
    ]

    for test in manual_tests:
        n, a, b = test
        ans, rules = solve(n, a, b)
        check_answer(n, a, b, ans, rules)

    random_tests = 50
    for i in range(random_tests):
        n = random.randint(1000, 100000)
        a = string_generator(n)
        b = string_generator(n)
        ans, rules = solve(n, a, b)
        check_answer(n, a, b, ans, rules)
