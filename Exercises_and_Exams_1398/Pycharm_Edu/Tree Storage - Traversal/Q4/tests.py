from test_helper import *
from task import *

if __name__ == '__main__':
    root1 = Node(1)
    root1.city1 = Node(2)
    root1.city2 = Node(3)
    root1.city1.city1 = Node(4)
    root1.city1.city2 = Node(5)
    root1.city2.city1 = Node(6)
    root1.city2.city2 = Node(7)
    root1.city2.city1.city2 = Node(8)
    root1.city2.city2.city2 = Node(9)

    root2 = Node(3)
    root2.city1 = Node(1)
    root2.city2 = Node(1)
    root2.city1.city1 = Node(0)
    root2.city1.city2 = Node(2)
    root2.city2.city1 = Node(0)
    root2.city2.city2 = Node(2)

    root3 = Node(1)
    root3.city1 = Node(2)
    root3.city2 = Node(2)
    root3.city1.city1 = Node(3)
    root3.city1.city2 = Node(4)
    root3.city2.city1 = Node(4)
    root3.city2.city2 = Node(3)
    root3.city1.city1.city1 = Node(5)
    root3.city1.city1.city2 = Node(6)
    root3.city1.city2.city1 = Node(7)
    root3.city1.city2.city2 = Node(8)
    root3.city2.city1.city1 = Node(8)
    root3.city2.city1.city2 = Node(7)
    root3.city2.city2.city1 = Node(6)
    root3.city2.city2.city2 = Node(5)

    root4 = Node(1)
    root4.city1 = Node(2)
    root4.city2 = Node(3)
    root4.city1.city1 = Node(4)
    root4.city2.city2 = Node(5)
    root4.city1.city1.city1 = Node(6)
    root4.city2.city2.city2 = Node(7)
    root4.city2.city2.city2.city1 = Node(8)
    root4.city2.city2.city2.city1.city1 = Node(9)
    root4.city2.city2.city2.city1.city1.city1 = Node(10)

    root5 = Node(1)
    root5.city1 = Node(2)
    root5.city2 = Node(3)
    root5.city1.city1 = Node(4)
    root5.city1.city2 = Node(5)
    root5.city1.city1.city1 = Node(6)
    root5.city1.city1.city1.city1 = Node(8)
    root5.city1.city2.city1 = Node(7)
    root5.city1.city2.city1.city1 = Node(9)

    tests = [
        (root1, 6),
        (root2, 5),
        (root3, 7),
        (root4, 10),
        (root5, 7)
    ]
    for test in tests:
        test_function(test[-1], solve, test[0])
