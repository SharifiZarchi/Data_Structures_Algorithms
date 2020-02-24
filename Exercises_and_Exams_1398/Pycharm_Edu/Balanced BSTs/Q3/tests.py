from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from random import shuffle
from random import randint
from task import func as func
from task_copy import func as func_judge

def test_generator(n):
    li = [i for i in range(n)]
    shuffle(li)
    return li
if __name__ == '__main__':
    test_nums = [10, 10, 100, 100, 10000]
    for test_num in test_nums:
        li = test_generator(test_num)
        user_li = func(li[0:len(li)])
        judge_li = func_judge(li[0:len(li)])
        if user_li != judge_li:
            failed("Wrong Answer! Input: " + str(li) +
                   " Your Answer: " + str(user_li) +
                   " Expected Answer: " + str(judge_li))
    print("PASS")


