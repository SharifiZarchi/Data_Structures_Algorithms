from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import *



if __name__ == '__main__':

    root = Node(10)
    root.left = Node(6)
    root.right = Node(14)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.right.left = Node(12)
    root.right.right = Node(1)

    if isbst(root):
        failed("please try again. 1")

    root = Node(10)
    root.left = Node(6)
    root.right = Node(14)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.right.left = Node(12)
    root.right.right = Node(16)
    if  isbst(root) is False:
        failed("please try again. 2")


