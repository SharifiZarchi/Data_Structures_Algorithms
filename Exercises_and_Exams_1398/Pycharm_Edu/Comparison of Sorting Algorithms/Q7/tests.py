from test_helper import *
from task import *

if __name__ == '__main__':
    tests = [
        (5, 6, [1, 2, 5, 10, 15, 20], 1),
        (4, 10, [1, 3, 2, 4], 0),
        (10, 100, [94, 65, 24, 47, 29, 98, 20, 65, 6, 17], 2)
    ]
    for test in tests:
        test_function(test[-1], func, test[0], test[1], test[2])
