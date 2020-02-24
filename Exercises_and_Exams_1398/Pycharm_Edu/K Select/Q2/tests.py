import random

from test_helper import *
from task import *

if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 5),
        ([10, 11, 12, 4, 3, 4, 1], 2, 4),
        ([1, 1, 1, 1, 1, 1, 3, 4, 6, 1], 7, 3),
        ([1], 0, 1),
        (random.sample(list(range(1000)), 1000), 221, 221),
        ([2, 5, 1, 7, 2, 5, 9, 8, 2, 0, 1, 5, 0], 12, 9)
    ]
    for test in tests:
        test_function(test[-1], find_kth, test[0], test[1])