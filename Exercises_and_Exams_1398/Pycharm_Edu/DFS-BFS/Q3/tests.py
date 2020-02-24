from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import *

if __name__ == '__main__':
    run_common_tests()
    g = graph(7)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(4,1)
    g.addEdge(2,6)
    g.addEdge(3,6)

    if maxDistance(g) != 4:
        failed("Wrong Answer")

    g = graph(4)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,0)
    if maxDistance(g) != 2:
        failed("Wrong Answer!")

    g.addEdge(0,2)
    g.addEdge(1,3)

    if maxDistance(g) != 1:
        failed("Wrong Answer!")

