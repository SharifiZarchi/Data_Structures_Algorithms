def insertion_sort(A):
    res = A[:]
    for k in range(1, len(res)):
        item = res[k]
        i = k
        while i > 0 and res[i-1] > item:
            res[i] = res[i-1]
            i -= 1
        res[i] = item
    return res


def selection_sort(A):
    res = A[:]
    n = len(res)
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if res[index] > res[j]:
                index = j
        res[i], res[index] = res[index], res[i]
    return res


def bubble_sort(A):
    res = A[:]
    n = len(res)
    for i in range(n-1):
        bubble_found = False
        for j in range(n-1, i, -1):
            if res[j] < res[j-1]:
                res[j], res[j-1] = res[j-1], res[j]
                bubble_found = True
        if not bubble_found:
            break
    return res


def bucket_sort(A):
    res = A[:]
    max_num = max(res)
    bucket_num = max_num // 10 + 1
    buckets = [[] for i in range(bucket_num)]
    
    for i in res:
        buckets[i // 10] += [i]

    for i in range(bucket_num):
        buckets[i] = selection_sort(buckets[i])

    res = []
    for i in range(bucket_num):
        res += buckets[i]
    
    return res


def radix_sort(A):
    res = A[:]
    max_num = max(res)
    radix = 1
    while radix <= max_num:
        B = [[] for i in range(10)]
        for i in res:
            B[int((i / radix) % 10)] += [i]
        res = []
        for i in range(10):
            res += B[i]
        radix *= 10
    return res