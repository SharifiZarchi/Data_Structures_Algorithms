# TODO: type solution here
from random import shuffle
class Node:
    def __init__(self, key=None, red=False, parent=None, children=None):
        self.key = key
        self.red = red
        self.parent = parent
        self.children = children

    def refresh_features(self):
        self.num_nodes = 1 + sum([child.num_nodes for child in self.children])
        self.sum_nodes = self.key + sum([child.sum_nodes for child in self.children])

    def get_direction(self):
        return 0 if self == self.parent.children[0] else 1

    def get_brother(self):
        return self.parent.children[1 - self.get_direction()]

    def get_uncle(self):
        return self.parent.get_brother()

    def make_black(self):
        self.red = False

    def make_red(self):
        self.red = True

class Tree:
    def __init__(self):
        self.dummy_parent = Node(children=[None])
        self.dummy_parent.children[0] = Node(parent=self.dummy_parent)
        self.nil = self.root
        self.nil.num_nodes = 0
        self.nil.sum_nodes = 0

    def insert(self, key):
        node = self.root
        node_parent = node.parent
        direction = 0
        while node != self.nil:
            node_parent = node
            direction = 0 if key < node.key else 1
            node = node.children[direction]
        #create new node
        node_parent.children[direction] = Node(key, red=True, parent=node_parent, children=[self.nil] * 2)
        #refresh features
        node = node_parent.children[direction]
        while node != self.root:
            node.refresh_features()
            node = node.parent

        self.cleanup_insert(node_parent.children[direction])

    def cleanup_insert(self, node):
        while node != self.root and node.parent.red:
            uncle = node.get_uncle()
            if uncle.red:
                uncle.make_black()
                node.parent.make_black()
                node.parent.parent.make_red()
                node = node.parent.parent
                continue
            #Save the value of grandparent because the rotation in the "if" staement below will mess up order of nodes
            grand_parent = node.parent.parent
            direction = node.get_direction()
            if direction != node.parent.get_direction():
                self.rotate(node.parent, 1 - direction)
                direction = 1 - direction
            self.rotate(grand_parent, 1 - direction)
            grand_parent.make_red()
            grand_parent.parent.make_black()
            #rotations should terminate loop
            break
        #Root should always be black
        self.root.make_black()

    def rotate(self, node, direction):
        child = node.children[1 - direction]
        midchild = child.children[direction]
        parent = node.parent

        parent.children[node.get_direction()] = child
        child.parent = parent

        child.children[direction] = node
        node.parent = child

        node.children[1 - direction] = midchild
        midchild.parent = node

        node.refresh_features()
        child.refresh_features()

    def in_order(self, node=None):
        if (node==None):
            node = self.root
        if node==self.nil:
            return []
        return self.in_order(node.children[0]) + [node] + self.in_order(node.children[1])

    def rank(self, key):
        node = self.root
        num_smaller_or_equal = 0
        while node != self.nil:
            if key < node.key:
                node = node.children[0]
                continue
            num_smaller_or_equal += node.children[0].num_nodes + 1
            if key > node.key:
                node = node.children[1]
            else:
                break
        return num_smaller_or_equal


    @property
    def root(self):
        return self.dummy_parent.children[0]

def func(li):
    total = 0
    x = Tree()
    for i in range(len(li)):
        total += i - x.rank(2 * li[i])
        x.insert(li[i])
    return total


