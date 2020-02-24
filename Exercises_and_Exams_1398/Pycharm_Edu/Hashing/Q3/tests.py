import random
import string
import task
from test_helper import failed


def sol(str):
    p, q = 27, 10 ** 9 + 7
    hash_list = sol_hash(str, q, p)
    offset = p
    for T in range(1, len(str)):
        if sol_is_period(hash_list, T, offset, q):
            return T
        offset = (offset * p) % q
    return None


def sol_is_period(hash_list, T, offset, q):
    return (hash_list[len(hash_list) - T - 1] * offset) % q == (hash_list[len(hash_list) - 1] - hash_list[T - 1]) % q


def sol_hash(str, q, p):
    hash_list = [ord(str[0]) - ord('a') + 1]
    s = 1
    for i in range(1, len(str)):
        s = (s * p) % q
        hash_list.append((hash_list[i - 1] + (ord(str[i]) - ord('a') + 1) * s) % q)
    return hash_list


def generate_test():
    T = random.randint(0, 10 ** 4)
    return ''.join(random.choice(string.ascii_lowercase) for i in range(T)) * (10 ** 5 // T)


if __name__ == '__main__':
    # put_limit(10)
    # try:
    for i in range(5):
        str = generate_test()
        if sol(str) != task.period(str):
            failed("Wrong Answer!")
    # except Exception:
    #     failed("Timed Out!")
