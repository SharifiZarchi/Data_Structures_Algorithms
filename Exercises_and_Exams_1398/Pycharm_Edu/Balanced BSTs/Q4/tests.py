from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from random import shuffle
from random import randint
from task import func as func
from task_copy import func as func_judge

def test_generator(n):
    li = []
    a_and_b_s = set()
    h_s = set()
    for i in range(n):
        max_range = 10000
        a = randint(1, max_range)
        b = randint(1, max_range)
        h = randint(1, max_range)
        # if a in a_and_b_s or b in a_and_b_s or h in h_s or a == b:
        #     continue
        # a_and_b_s.add(a)
        # a_and_b_s.add(b)
        # h_s.add(h)
        if a == b:
            continue
        if a > b:
            a, b = b, a
        li.append((a, h, b))
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


