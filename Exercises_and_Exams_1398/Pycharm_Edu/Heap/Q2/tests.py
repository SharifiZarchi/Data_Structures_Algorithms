from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import *

if __name__ == '__main__':
    mat = [ [1, 3, 5, 7],
            [2, 4, 6, 8],
            [0, 9, 10, 11] ]
    arr = merge_k_sorted_arrays(mat, 3, 4)
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        failed("Wrong Answer!")

    mat = [ [-2, 3, 5, 10, 11, 100],
            [1, 3, 5, 6, 7, 8],
            [-3, -2, -1, 101, 102, 103],
            [0, 0, 0, 0, 0, 105]]
    arr = merge_k_sorted_arrays(mat, 4, 6)
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        failed("Wrong Answer!")
