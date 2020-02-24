# TODO: type solution here
class Node:
    def __init__(self, key=None, red=False, parent=None, children=None):
        self.key = key
        self.red = red
        self.parent = parent
        self.children = children
        self.num_nodes = 0
        self.sum_nodes = 0

    def refresh_features(self):
        self.num_nodes = 1 + sum([child.num_nodes for child in self.children])
        self.sum_nodes = self.key.value + sum([child.sum_nodes for child in self.children])

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
        # create new node
        node_parent.children[direction] = Node(key, red=True, parent=node_parent, children=[self.nil] * 2)
        # refresh features
        node = node_parent.children[direction]
        while node != self.dummy_parent:
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
            # Save the value of grandparent because the rotation in the "if" staement below will mess up order of nodes
            grand_parent = node.parent.parent
            direction = node.get_direction()
            if direction != node.parent.get_direction():
                self.rotate(node.parent, 1 - direction)
                direction = 1 - direction
            self.rotate(grand_parent, 1 - direction)
            grand_parent.make_red()
            grand_parent.parent.make_black()
            # rotations should terminate loop
            break
        # Root should always be black
        self.root.make_black()

    def rotate(self, node, direction):
        child = node.children[1 - direction]
        mid_child = child.children[direction]
        parent = node.parent

        parent.children[node.get_direction()] = child
        child.parent = parent

        child.children[direction] = node
        node.parent = child

        node.children[1 - direction] = mid_child
        mid_child.parent = node

        node.refresh_features()
        child.refresh_features()

    def in_order(self, node=None):
        if node is None:
            node = self.root
        if node == self.nil:
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

    def increase_value(self, key, amount):
        node = self.root
        while node != self.nil:
            if key < node.key.key:
                node = node.children[0]
            elif key > node.key.key:
                node = node.children[1]
            else:
                break
        if node == self.nil:
            self.insert(My_pair(key, amount))
        else:
            node.key.value += amount
            while node != self.dummy_parent:
                node.refresh_features()
                node = node.parent

    def sum_range_zero(self, key):
        node = self.root
        sum_smaller_or_equal = 0
        while node != self.nil:
            if key < node.key:
                node = node.children[0]
                continue
            sum_smaller_or_equal += node.sum_nodes - node.children[1].sum_nodes
            if key > node.key:
                node = node.children[1]
            else:
                break
        return sum_smaller_or_equal

    @property
    def root(self):
        return self.dummy_parent.children[0]


class My_pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def increment_value(self):
        self.value += 1

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __eq__(self, other):
        if self is None or other is None:
            return self is None and other is None
        return self.key == other.key

    def __ne__(self, other):
        return not self == other


def data_structure(li):
    x = Tree()
    output = []
    for cmd in li:
        if cmd[0] == 1:
            num = int(cmd[1])
            amount = int(cmd[2])
            x.increase_value(num, amount)
        else:
            num = int(cmd[1])
            output.append(x.sum_range_zero(My_pair(num, None)))
    return output
