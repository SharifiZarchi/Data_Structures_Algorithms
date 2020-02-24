from test_helper import *
from task import *


def intersect(l1, r1, l2, r2):
    if l1 <= l2 and r1 >= r2 or l2 <= l1 and r2 >= r1:
        return False
    if r2 <= r1 and l1 <= l2 and r2 <= l2:
        return False
    if l1 >= r2 and l1 >= l2 or r1 <= l2 and r1 <= r2:
        return False
    return True


def check_fallacy(l1, r1, l2, r2, ans1, ans2):
    if intersect(l1, r1, l2, r2):
        return ans1 == ans2
    return False


def dfs(v, clr, color, graph):
    if color[v] != -1 and color[v] != clr:
        return 'Impossible'
    if color[v] != -1:
        return
    color[v] = clr
    for u in graph[v]:
        if dfs(u, 1 - clr, color, graph) == 'Impossible':
            return 'Impossible'


def my_solve(input):
    n, m = input[0]
    graph = [[] for i in range(m)]
    vedge = []
    color = [-1] * m
    for i in range(m):
        a, b = map(int, input[i + 1])
        a, b = min(a, b), max(a, b)
        for j, v in enumerate(vedge):
            if intersect(a, b, v[0], v[1]):
                graph[i].append(j)
                graph[j].append(i)
        vedge.append((a, b))

    for i in range(m):
        if color[i] == -1:
            if dfs(i, 0, color, graph):
                return 'Impossible'
    return answer(color)


def answer(color):
    return str(['I' if i == 0 else 'O' for i in color])


if __name__ == '__main__':
    in1 = [[4, 2], [1, 3], [2, 4]]
    in2 = [[5, 2], [2, 4], [4, 1]]
    in3 = [[6, 6], [1, 4], [4, 6], [2, 6], [2, 4], [5, 3], [6, 3]]
    in4 = [[17, 10], [4, 11], [7, 16], [8, 5], [12, 15], [7, 4], [1, 12], [11, 1], [15, 1], [7, 14], [2, 9]]

    tests = [in1, in2, in3, in4]
    for test in tests:
        ans = solve(test)
        true_ans = my_solve(test)
        if true_ans == 'Impossible':
            if ans == 'Impossible':
                continue
            else:
                failed("Wrong Answer! Input: {}, your output: {}, answer: {}".format(test, ans, my_solve(test)))
        for i in range(1, len(test)):
            for j in range(i + 1, len(test)):
                if check_fallacy(test[i][0], test[i][1], test[j][0], test[j][1], list(ans)[i - 1], list(ans)[j - 1]):
                    failed("Wrong Answer! Input: {}, your output: {}, answer: {}".format(test, ans, my_solve(test)))
                passed()
