#!/usr/bin/env python3
import sys
import timeit
from typing import List
def counter(a: List[int]) -> int:
    N:int = len(a)
    counter:int = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                s = a[i] + a[j] + a[k]
                if s == 0:
                    counter += 1
    return counter

if __name__ == "__main__":
    int_count = sys.argv[1]
    with open(f"data/{int_count}ints.txt", "r") as data:
        arr: List[int] = [int(line.strip()) for line in data.readlines()]
        number:int = 2
        def to_call():
            return counter(arr)
        result = timeit.timeit(to_call, number=number)
        print(
            f"{number} вызовов для {int_count} данных: лучший результат равен {result:.02f}"
        )
