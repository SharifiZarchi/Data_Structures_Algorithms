from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import *

if __name__ == '__main__':
    run_common_tests()
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    if not hasCycle(g):
        failed("Wrong Answer!")

    g = Graph(3)
    g.addEdge(0,1)
    g.addEdge(1,2)

    if hasCycle(g):
        failed("Wrong Answer!")

    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(3, 4)
    g.addEdge(3, 2)
    g.addEdge(3, 1)

    if not hasCycle(g):
        failed("Wrong Answer!")


