def insertion_sort(A):
    for k in range(1, len(A)):

        item = A[k]

        i = k       
        while i > 0 and A[i-1] > item:
            A[i] = A[i-1]

            i -= 1
        A[i] = item
    res = A
    return res

def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        index = i

        for j in range(i+1, n):      
            if A[index] > A[j]:

                index = j
        A[i], A[index] = A[index], A[i]             

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
        if not bubble_found:

            break
    res = A
    return res

def get_bucket(x):
    return x // 10

def bucket_sort(A):

    max_num = max(A)
    bucket_num = get_bucket(max_num) + 1
    buckets = [[] for i in range(bucket_num)]

    for i in A:
        buckets[get_bucket(i)] += [i]

    for i in range(bucket_num):
        buckets[i] = selection_sort(buckets[i])
    res = []
    for i in range(bucket_num):
        res += buckets[i]

    return res

def radix_sort(A):

    max_num = max(A)
    radix = 1

    while radix <= max_num:
        B = [[] for i in range(10)] 

        for i in A:
            B[(i//radix)%10] += [i]

        A = []

        for i in range(10):
            A += B[i]

        radix *= 10

    return A

if __name__ == '__main__':
    A = [1523, 1, 19, 3229, 4, 16, 25, 909, 223, 1648]
    
    print("insertion sort",insertion_sort(A))

    print("selection sort",selection_sort(A))

    print("bubble sort",bubble_sort(A))

    print("bucket sort",bucket_sort(A))
    
    print("radix sort",radix_sort(A))
