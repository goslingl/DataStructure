import numpy as np
import random

def check_sort_result(A):
    for idx in range(len(A)-1):
        if A[idx+1] < A[idx]:
            break
    else:
        return True
    return False

def sort():
    A = list(range(100000)) + list(range(100000))
    np.random.shuffle(A)
    qsort(A, 0, len(A)-1)
    #qsort2(A, 0, len(A)-1)
    s = check_sort_result(A)
    print('qsort result:', s)
    print('A:', A[:10], A[-10:])

def qsort(A, st, ed):
    '''
    @Desc: 关键点，参考元素在最左边，则先右后左比较；参考元素在最右边，则先左后右比较
    '''
    if st >= ed: return
    mid = (st+ed)//2
    #A[mid], A[st] = A[st], A[mid]
    #flag = A[st]
    A[mid], A[ed] = A[ed], A[mid]
    flag = A[ed]
    i, j = st, ed
    while i < j:
        while i < j and A[i] <= flag:
            i += 1
        while i < j and A[j] >= flag:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    #A[i], A[st] = A[st], A[i]
    A[i], A[ed] = A[ed], A[i]
    qsort(A, st, i-1)
    qsort(A, i+1, ed)

def qsort2(A, st, ed):
    if st >= ed: return
    flag = A[st]
    i, j = st, ed
    while i < j:
        while i < j and A[j] >= flag:
            j -= 1
        while i < j and A[i] <= flag:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[st], A[i] = A[i], A[st]
    qsort2(A, st, i-1)
    qsort2(A, i+1, ed)

sort()

