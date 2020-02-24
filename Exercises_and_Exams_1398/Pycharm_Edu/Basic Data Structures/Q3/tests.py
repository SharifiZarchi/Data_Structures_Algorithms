from test_helper import *
from task import *
import random


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def check_swap(array_list, i, j):
    print(i, j)
    linked_list_swap(array_list[i], array_list[j])
    array_list[i], array_list[j] = array_list[j], array_list[i]
    error = False
    for k in range(0, len(array_list) - 1):
        if array_list[k].next != array_list[k + 1] or array_list[-k - 1].prev != array_list[-k - 2]:
            error = True
    if array_list[0].prev != None or array_list[-1].next != None or error:
        if abs(i - j) == 1:
            failed("Wrong linked list. Input is adjacent nodes.")
        elif i == 0 or j == 0 or i == len(array_list) - 1 or j == len(array_list) - 1:
            failed("Wrong linked list. Input contains head or tail nodes.")
        else:
            failed("Wrong linked list. Input isn't adjacent or head or tail nodes.")


if __name__ == '__main__':
    prev = Node(random.random())
    array_list = [prev]
    for i in range(1, 100):
        new = Node(random.random())
        new.prev = prev
        prev.next = new
        prev = new
        array_list.append(new)

    check_swap(array_list, 44, 88)
    check_swap(array_list, 0, 10)
    check_swap(array_list, 99, 5)
    check_swap(array_list, 0, 99)
    check_swap(array_list, 64, 65)
    check_swap(array_list, 9, 8)
    check_swap(array_list, 98, 99)
    check_swap(array_list, 1, 0)
