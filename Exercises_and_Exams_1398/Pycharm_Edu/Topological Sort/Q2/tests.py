from test_helper import *
from task import *

if __name__ == '__main__':
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]
    row = len(graph)
    col = len(graph[0])
    g = Graph(row, col, graph)

    graph = [[1, 1],
             [1, 1]]
    row = len(graph)
    col = len(graph[0])
    g2 = Graph(row, col, graph)

    graph = [[0 for i in range(1000)] for j in range(1000)]
    row = col = 1000
    g3 = Graph(row, col, graph)

    graph = [[0 for i in range(1000)] for j in range(1000)]
    graph[500] = [(1 if i % 2 == 0 else 0) for i in range(1000)]
    print(graph[500])
    row = col = 1000
    g4 = Graph(row, col, graph)

    tests = [
        (g, 5),
        (g2, 1),
        (g3, 0),
        (g4, 500),
    ]
    for test in tests:
        my_test_function(test[-1], solve, test[0])
