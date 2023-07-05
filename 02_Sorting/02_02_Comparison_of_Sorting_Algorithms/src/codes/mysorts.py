def insertion_sort(A):
    for k in range(1, len(A)):
        item = A[k]
        i = k
        while i > 0 and A[i-1] > item:
            A[i] = A[i-1]
            i -= 1
        A[i] = item
    return A


def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if A[index] > A[j]:
                index = j
        A[i], A[index] = A[index], A[i]
    return A


def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        bubble_found = False
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                bubble_found = True
        if not bubble_found:
            break
    return A


def bucket_sort(A):
    max_num = max(A)
    bucket_num = max_num // 10 + 1
    buckets = [[] for i in range(bucket_num)]
    
    for i in A:
        buckets[i // 10] += [i]

    for i in range(bucket_num):
        buckets[i] = selection_sort(buckets[i])

    A = []
    for i in range(bucket_num):
        A += buckets[i]
    
    return A


def radix_sort(A):
    max_num = max(A)
    radix = 1
    while radix <= max_num:
        B = [[] for i in range(10)]
        for i in A:
            B[int((i / radix) % 10)] += [i]
        A = []
        for i in range(10):
            A += B[i]
        radix *= 10
    return A