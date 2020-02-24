from test_helper import *
from task import *

if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(2)
    root1.left.left = Node(3)
    root1.left.right = Node(4)
    root1.right.left = Node(4)
    root1.right.right = Node(3)

    root2 = Node(3)
    root2.left = Node(1)
    root2.right = Node(1)
    root2.left.left = Node(0)
    root2.left.right = Node(2)
    root2.right.left = Node(0)
    root2.right.right = Node(2)

    root3 = Node(1)
    root3.left = Node(2)
    root3.right = Node(2)
    root3.left.left = Node(3)
    root3.left.right = Node(4)
    root3.right.left = Node(4)
    root3.right.right = Node(3)
    root3.left.left.left = Node(5)
    root3.left.left.right = Node(6)
    root3.left.right.left = Node(7)
    root3.left.right.right = Node(8)
    root3.right.left.left = Node(8)
    root3.right.left.right = Node(7)
    root3.right.right.left = Node(6)
    root3.right.right.right = Node(5)

    root4 = Node(1)
    root4.left = Node(2)
    root4.right = Node(2)
    root4.left.left = Node(3)
    root4.left.right = Node(4)
    root4.right.left = Node(4)
    root4.right.right = Node(3)
    root4.left.left.left = Node(5)
    root4.left.left.right = Node(6)
    root4.left.right.left = Node(7)
    root4.left.right.right = Node(8)
    root4.right.left.left = Node(8)
    root4.right.left.right = Node(7)
    root4.right.right.left = Node(5)
    root4.right.right.right = Node(6)
    tests = [
        (root1, True),
        (root2, False),
        (root3, True),
        (root4, False)
    ]
    for test in tests:
        test_function(test[-1], isSymmetric, test[0])
