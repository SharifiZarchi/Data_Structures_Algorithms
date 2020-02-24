from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import *

if __name__ == '__main__':
    run_common_tests()
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
    if countPaths(g, 2, 3) != 3:
        failed("Wrong Answer!")

    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,4)
    g.addEdge(1,3)
    g.addEdge(1,4)
    g.addEdge(2,4)
    g.addEdge(3,2)

    if countPaths(g, 0, 4) != 4:
        failed("Wrong Answer!")

    if countPaths(g, 1, 0) != 0:
        failed("Wrong Answer!")
