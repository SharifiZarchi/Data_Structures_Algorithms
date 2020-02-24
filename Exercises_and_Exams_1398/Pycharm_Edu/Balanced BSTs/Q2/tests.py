from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from random import shuffle
from random import randint
from task import data_structure as func
from task_copy import data_structure as func_judge


def test_generator(n):
    li = []
    for i in range(n):
        kind = randint(1, 2)
        max_range = 10000
        if kind == 1:
            li.append((1, randint(1, max_range), randint(1, max_range)))
        else:
            li.append((2, randint(1, max_range)))
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


