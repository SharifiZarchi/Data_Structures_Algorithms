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
    #Implement the function
