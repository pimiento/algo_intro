#!/usr/bin/env python3
import sys
import timeit
from typing import List


def sort_alg(l):
  for i in range(len(l)):
    for j in range(len(l[i+1:])):
      if l[j] > l[j+1]:
        l[j], l[j+1] = (l[j+1], l[j])
  return l

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
