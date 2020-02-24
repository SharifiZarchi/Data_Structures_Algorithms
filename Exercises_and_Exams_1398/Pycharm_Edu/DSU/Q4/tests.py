from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from test_helper import *
from task import *
import random


def solve2(n, numbers, perm):
    # numbers is a list of n integers
    # perm is a list of the numbers 1 to n in some permutation
    # Return a list of answers

    perm2 = [i - 1 for i in perm]
    perm = perm2
    answers = []
    current_answer = 0
    dsu = DisjointSet(n)

    def add(i, current_answer):
        node = dsu.nodes[i]
        node.added = True
        node.sum = numbers[i]
        if i > 0 and dsu.nodes[i - 1].added:
            dsu.unite(node, dsu.nodes[i - 1])
        if i < n - 1 and dsu.nodes[i + 1].added:
            dsu.unite(node, dsu.nodes[i + 1])

        parent = dsu.find(node)
        current_answer = max(current_answer, parent.sum)
        return current_answer

    for i in range(n - 1, -1, -1):
        answers.append(current_answer)
        current_answer = add(perm[i], current_answer)

    answers.reverse()
    return answers


if __name__ == '__main__':
    manual_tests = [
        (4, [1, 3, 2, 5], [3, 4, 1, 2], [5, 4, 3, 0]),
        (5, [1, 2, 3, 4, 5], [4, 2, 3, 5, 1], [6, 5, 5, 1, 0]),
        (8, [5, 5, 4, 4, 6, 6, 5, 5], [5, 2, 8, 7, 1, 3, 4, 6], [18, 16, 11, 8, 8, 6, 6, 0]),
        (10, [3, 3, 3, 5, 6, 9, 3, 1, 7, 3], [3, 4, 6, 7, 5, 1, 10, 9, 2, 8], [34, 29, 14, 11, 11, 11, 8, 3, 1, 0]),
        (17, [12, 9, 17, 5, 0, 6, 5, 1, 3, 1, 17, 17, 2, 14, 5, 1, 17],
         [3, 7, 5, 8, 12, 9, 15, 13, 11, 14, 6, 16, 17, 1, 10, 2, 4],
         [94, 78, 78, 77, 39, 39, 21, 21, 21, 21, 21, 21, 21, 9, 9, 5, 0]),
        (17, [1, 6, 9, 2, 10, 5, 15, 16, 17, 14, 17, 3, 9, 8, 12, 0, 2],
         [9, 13, 15, 14, 16, 17, 11, 10, 12, 4, 6, 5, 7, 8, 2, 3, 1],
         [65, 64, 64, 64, 64, 64, 64, 64, 64, 46, 31, 31, 16, 16, 9, 1, 0]),
        (17, [10, 10, 3, 9, 8, 0, 10, 13, 11, 8, 11, 1, 6, 9, 2, 10, 5],
         [9, 4, 13, 2, 6, 15, 11, 5, 16, 10, 7, 3, 14, 1, 12, 8, 17],
         [63, 52, 31, 31, 26, 23, 23, 23, 23, 23, 13, 13, 13, 13, 13, 5, 0]),
        (10,
         [606976827, 581094359, 726836550, 554157795, 277900063, 389778978, 555756858, 259222039, 862348978, 749561490],
         [10, 8, 9, 5, 2, 1, 6, 3, 4, 7],
         [4814072447, 3692501430, 3692501430, 2469065531, 1280994345, 1280994345, 1280994345, 555756858, 555756858, 0]),
    ]

    for test in manual_tests:
        test_function(test[-1], solve, test[0], test[1], test[2])

    random_tests = 100
    for i in range(random_tests):
        n = random.randint(1000, 10000)
        nums = []
        for i in range(n):
            nums.append(random.randint(0, 1000000000))
        perm = list(range(1, n + 1))
        random.shuffle(perm)
        x = solve2(n, nums, perm)
        test_function(x, solve, n, nums, perm)
