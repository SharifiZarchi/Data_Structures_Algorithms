from rb_tree import RedBlackTree
from random import shuffle

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

def main():
    n = 10
    li = [i for i in range(n)]
    shuffle(li)
    print(li)
    print(func(li))

def func(li):
    tree = RedBlackTree()
    depths = []
    for num in li:
        next_node = tree.ceil(My_pair(num, None))
        prev_node = tree.floor(My_pair(num, None))
        parent_depth = -1
        for node in (next_node, prev_node):
            if node != None:
                parent_depth = max(parent_depth, node.value)
        tree.add(My_pair(num, parent_depth + 1))
        depths.append(parent_depth + 1)
    return depths





if __name__ == '__main__':
    main()
