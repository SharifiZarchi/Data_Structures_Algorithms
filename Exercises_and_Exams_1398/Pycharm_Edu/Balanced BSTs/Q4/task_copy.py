# TODO: type solution here
from rb_tree import RedBlackTree

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


#li elements are in (a, b, h) form
def func(li):
    li.sort(key=lambda x:x[1])
    tree = RedBlackTree()
    for a, h, b in li:
        prev_b = tree.floor(My_pair(b, None))
        if prev_b is None:
            height_b = 0
        else:
            height_b = prev_b.value

        next_a = tree.ceil(My_pair(a, None))
        while (next_a is not None) and next_a.key <= b:
            tree.remove(next_a)
            next_a = tree.ceil(My_pair(a, None))

        tree.add(My_pair(a, h))
        tree.add(My_pair(b, height_b))

    prev_height = 0
    ans = []
    for element in tree:
        if element.value != prev_height:
            prev_height = element.value
            ans.append((element.key, element.value))
    return ans
