def counting_sort(A):
    m = max(A) 
    Count = [0] * (m + 1)
    for x in A:
        Count[x] += 1  # counting elements of array
    A = []
    for i in range(m + 1):
        A += [i] * Count[i]

    return A


def insertion_sort(A):
    for k in range(1, len(A)):
        item = A[k]
        i = k
        while i > 0 and A[i-1] > item:
            A[i] = A[i-1]
            i -= 1
        A[i] = item
    return A

def bubble_sort(A):
    n = len(A)
    for i in range(n - 1):  # iterate for each element in array
        bubble_found = False
        for j in range(n - 1, i, -1):  # iterate for sort a element in right place
            if A[j] < A[j - 1]:
                A[j] , A[j-1] = A[j-1], A[j] # Swap Bubble
                bubble_found = True
        if not bubble_found:
            break # No bubble found
        
    return A

def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        index = i
        for j in range(i+1, n): # iterate for finding min remaining item
            if A[index] > A[j]:
                index = j
        
        A[index], A[i] = A[i], A[index]

    return A


def bucket_sort(A):
    def get_bucket(x):
        return x // 10

    m = max(A)
    bucket_num = get_bucket(m)
    buckets = [[] for i in range(bucket_num + 1)] # create bucket for clustering theory
    
    for i in A:
        buckets[get_bucket(i)] += [i] # add elements to buckets

    for j in range(bucket_num): # sorting each element
        buckets[j] = bubble_sort(buckets[j])

    A = []
    for k in buckets: # concat each sorted bucket
        A += k
    return A


def merge_sort(A):
    if len(A) < 2:
        return A
    mid = len(A)//2

    B = A[mid:]
    C = A[:mid]

    B = merge_sort(B)

    C = merge_sort(C)
    return B, C


if __name__ == '__main__':
    A = [5, 1, 1, 1, 2, 5, 3, 4, 4, 2, 3]
    print('counting sort',counting_sort(A))

    A = [5, 2, -3, 4, 6, -7, 1, 9, 12, 5, -6]
    print('insertion sort',insertion_sort(A))

    A = [5, 12, 3, 4, 7, 1, 0, 6, 19, 8, 13, 4, 2, 10, 16]
    print('bubble_sort', bubble_sort(A))

    A = [12, 3, 15, -4, 7, 6, -1, 0, 11, 6]
    print('selection_sort', selection_sort(A))

    A = [29, 25, 9, 49, 3, 37, 21, 43]
    print('bucket sort', bucket_sort(A))

    A = [12, 3, 15, -4, 7, 6, -1, 0, 11, 6]
    print('merge sort', merge_sort(A))
