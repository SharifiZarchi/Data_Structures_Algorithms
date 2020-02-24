from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import*


if __name__ == "__main__":

    pre = [8, 3, 5, 7, 6]
    size = len(pre)

    if (hasOnlyOneChild(pre, size) == False):
        failed("please try again")



    pre = [11, 10, 6, 8, 3]
    size = len(pre)
    if (hasOnlyOneChild(pre, size) == True):
        failed("please try again")
