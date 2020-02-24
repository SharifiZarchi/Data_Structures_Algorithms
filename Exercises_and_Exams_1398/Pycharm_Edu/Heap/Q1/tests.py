from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import *

if __name__ == '__main__':
    n = 10
    arr1 = "0 0 0 0 1 0 1 0 1"
    arr2 = "5 10 17 6 2 1 3 2 4"
    if maxVahed(n,arr1,arr2) != 20:
        failed("Wrong Answer")

    n = 6
    arr1 = "0 0 1 0 1"
    arr2 = "10 12 2 1 3"

    if maxVahed(n,arr1,arr2) != 13:
        failed("Wrong Answer")
