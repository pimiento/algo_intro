#!/usr/bin/env python3
import sys
import timeit
from typing import List

def binary_search(
        lst:List[int], target:int
) -> int:
    start:int = 0
    end:int = len(lst) - 1
    while(start <= end):
        mid = (start + end) // 2
        if(lst[mid] > target):
            end = mid - 1
        elif(lst[mid] < target):
            start = mid + 1
        else:
            return mid
    return -1

def counter(a: List[int]) -> int:
  # O(NlogN)
  arr:List[int] = sorted(a)
  N:int = len(arr)
  counter:int = 0
  for i in range(N):
    for j in range(i+1, N):
      # O(logN)
      if binary_search(
        arr, -(arr[i]+arr[j])
      ) > j:
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
