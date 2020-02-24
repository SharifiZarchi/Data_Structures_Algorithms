from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from task import *

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()



#intersection in O(m + n)
# m is size of arr1, n is size of array2
finalarray = []
def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        i, j = 0, 0
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr1[i]:
                j += 1
            else:
                # common element.
                finalarray.append(arr2[j])
                j += 1
                i += 1


if __name__ == '__main__':
    mainroot = Node(5)
    insert(mainroot,1)
    insert(mainroot,3)
    insert(mainroot,6)
    insert(mainroot,8)
    insert(mainroot,7)
    insert(mainroot, 4)

    mainroot2 = Node(10)
    insert(mainroot2, 11)
    insert(mainroot2, 4)
    insert(mainroot2, 6)
    insert(mainroot2, 7)
    insert(mainroot2, 14)
    insert(mainroot2, 9)

    inorder1 = []
    inorder2 = []
    inordertraversal(mainroot, inorder1)
    inordertraversal(mainroot2, inorder2)

    m = len(inorder1)
    n = len(inorder2)
    printIntersection(inorder1, inorder2, m, n)

    for i in [4,6,7]:
        if i not in finalarray:
            failed("try again")




