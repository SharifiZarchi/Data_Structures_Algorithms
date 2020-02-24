from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import *

if __name__ == '__main__':
    run_common_tests()

    n = 7
    arr = "7 2 3 13 5 17 11"
    q = 4
    inp = ["3 7", "2 5", "0 7", "5 6"]

    if func(n, arr, q, inp) != [5, 3, 2, 17]:
        failed("Wrong Answer!")


