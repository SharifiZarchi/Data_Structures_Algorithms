from test_helper import *
from task import *
from testcases import tests

if __name__ == '__main__':
    for test in tests:
        test_function(test[0], solve, test[1], test[2], test[3])
