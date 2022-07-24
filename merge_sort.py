#!/usr/bin/env python3
import sys
import timeit
from typing import List


def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A

def sort_alg(A):
    return merge_sort(A)

if __name__ == "__main__":
    int_count = sys.argv[1]
    with open(f"data/{int_count}ints.txt", "r") as data:
        arr: List[int] = [int(line.strip()) for line in data.readlines()]
        number:int = 2
        def to_call():
            return sort_alg(arr)
        result = timeit.timeit(to_call, number=number)
        print(
            f"{number} вызовов для {int_count} данных: лучший результат равен {result:.02f}"
        )
