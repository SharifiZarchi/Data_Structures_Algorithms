import task
import random
import string
from test_helper import failed


def sol_setup(dictionary):
    global words
    words = set(dictionary)


def sol_suggestions(word):
    result = set()
    is_legit = word in words
    if not is_legit:
        # add char
        for i in range(len(word) + 1):
            for char in string.ascii_lowercase:
                possible = word[:i] + char + word[i:]
                if possible in words:
                    result.add(possible)
        # remove char
        for i in range(len(word)):
            possible = word[:i] + word[i + 1:]
            if possible in words:
                result.add(possible)
        # change char
        for i in range(len(word)):
            for char in string.ascii_lowercase:
                possible = word[:i] + char + word[i + 1:]
                if possible in words:
                    result.add(possible)
    return is_legit, result


if __name__ == '__main__':
    task.setup({"abc", "abcd", "g", "e", "ggh"})
    if task.suggestions("ggh") != (True, set()):
        failed("Wrong Answer!")
    if task.suggestions("abcz") != (False, {"abcd", "abc"}):
        failed("Wrong Answer!")
    if task.suggestions("gh") != (False, {"g", "ggh"}):
        failed("Wrong Answer!")
    if task.suggestions("a") != (False, {"g", "e"}):
        failed("Wrong Answer!")
    if task.suggestions("bbb") != (False, set()):
        failed("Wrong Answer!")
    if task.suggestions("bbc") != (False, {"abc"}):
        failed("Wrong Answer!")
    dic = {''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 50))) for _ in range(10000)}
    test = {''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 10))) for _ in range(10000)}
    task.setup(dic)
    sol_setup(dic)
    for word in test:
        if task.suggestions(word) != sol_suggestions(word):
            failed("Wrong Answer!")
