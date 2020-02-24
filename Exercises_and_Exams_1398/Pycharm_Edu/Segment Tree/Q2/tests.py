from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import *

if __name__ == '__main__':
    run_common_tests()

    n = "0 0 1 0 1 0 1 1 1 0"
    q = 8
    inp = ["s 3 7", "g 4", "s 2 8", "s 5 10", "g 4", "s 0 6", "g 3", "g 5"]

    if func(n,q,inp) != [0, 1, 1, 0]:
        failed("Wrong Answer!")


