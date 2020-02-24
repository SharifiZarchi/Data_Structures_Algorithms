from test_helper import *
from task import *

if __name__ == '__main__':
    tests = [
        ([1, 2, 3], True),
        ([3, 2, 1], True),
        ([2, 3, 1], False),
        ([3, 1, 2], True),
        ([1, 10, 5, 6, 4, 9, 8, 7, 3, 2], False),
        ([6, 5, 1, 2, 4, 3], True)
    ]
    for test in tests:
        test_function(test[-1], can_sort_by_stack, test[0])
