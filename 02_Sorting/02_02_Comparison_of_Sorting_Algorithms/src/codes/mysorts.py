def insertion_sort(A):
    for k in range(1, len(A)):       # Insert all elements 2 to n
        item = A[k]             # The k'th element to be inserted
        i = k             # i will hold the position of insertion
        while i > 0 and A[i-1] > item:
            A[i] = A[i-1]                        # Shift to right
            i -= 1
        A[i] = item
    res = A
    return res

def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        index = i           # The index of min remaining item
        for j in range(i+1, n):      
            if A[index] > A[j]:  # Finding min remaining item
                index = j
        A[i], A[index] = A[index], A[i]                # Swap
    res = A
    return res



def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        bubble_found = False
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1], A[j]
                bubble_found = True
        if not bubble_found:     # Stopping when array is sorted
            break
    res = A
    return res


if __name__ == '__main__':
    A = [33750, 11161, 20704, 60193, 19536]
    selection_sort(A)
    bubble_sort(A)