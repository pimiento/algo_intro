- [Зачем нужны алгоритмы?](#orgeb949a9)
  - [Задача](#orga9d47f3)
- [Зачем нужны алгоритмы?](#orgcecd020)
- [Результат наивной реализации](#org2e37005)
- [Бинарный поиск](#org1c5050a)
- [Быстрый ThreeSum](#org0cef2fc)
- [Рузельтат быстрого ThreeSum](#org33d9a43)
- [Алгоритмическая сложность](#orgc319fec)
- [Нужны ли алгоритмы backend-разработчику?](#orgda2913b)
- [Какие алгоритмы нужнее всего?](#org947612d)
  - [Зависит от задачи, области применения](#org0b16889)
- [Структуры данных. Очередь](#org449d9fa)
- [Структуры данных. Стек](#org8362a04)
- [Структуры данных. Граф](#orgbb8e2c3)
- [Поиск вглубину. Depth-First Search](#org48c37f7)
- [Глупая сортировка / сортировка дурака](#orgcbdf209)
- [Результат глупой сортировки](#org766c766)
- [Пузырьковая сортировка](#orge7be6d4)
- [Результат пузырьковой сортировки](#org9ea601c)
- [Сортировка слиянием (Merge Sort)](#org4500b9a)
- [Результат Merge Sort](#org113bba5)
- [Сравнение алгоритмов сортировки](#org2bdedf9)
- [Устойчивость сортировки](#org2ae34f2)
- [Как изучать алгоритмы](#orgbde7591)



<a id="orgeb949a9"></a>

# Зачем нужны алгоритмы?


<a id="orga9d47f3"></a>

## Задача

Подсчитать, какое количество сочетаний по три элементов входного массива даст в сумме 0.  


<a id="orgcecd020"></a>

# Зачем нужны алгоритмы?

```python

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


```


<a id="org2e37005"></a>

# Результат наивной реализации

>   % python ./first\_try.py 1K  
> 2 вызовов для 1K данных: лучший результат равен 42.02  
>   % python ./first\_try.py 2K  
> 2 вызовов для 2K данных: лучший результат равен 340.84  


<a id="org1c5050a"></a>

# Бинарный поиск

```python


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
```


<a id="org0cef2fc"></a>

# Быстрый ThreeSum

```python


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

```


<a id="org33d9a43"></a>

# Рузельтат быстрого ThreeSum

>   % python fast\_threesum.py 1K  
> 2 вызовов для 1K данных: лучший результат равен 1.64  
>   % python fast\_threesum.py 2K  
> 2 вызовов для 2K данных: лучший результат равен 7.36  
>   % python fast\_threesum.py 4K  
> 2 вызовов для 4K данных: лучший результат равен 31.31  


<a id="orgc319fec"></a>

# Алгоритмическая сложность

![img](/home/pimiento/yap/order_of_growth.png)  


<a id="orgda2913b"></a>

# Нужны ли алгоритмы backend-разработчику?

![img](/home/pimiento/yap/algorithms_for_kids.png)  


<a id="org947612d"></a>

# Какие алгоритмы нужнее всего?


<a id="org0b16889"></a>

## Зависит от задачи, области применения

-   алгоритмы на строках  
    нужны например биоинформатикам, для работы с последовательностями ДНК
-   алгоритмы на деревьях  
    -   компиляторы
    -   машинное обучение
    -   построение маршрутов
    -   парсинг сайтов


<a id="org449d9fa"></a>

# Структуры данных. Очередь

-   **FIFO:** First In First Out

![img](/home/pimiento/yap/Fifo_queue.png)  


<a id="org8362a04"></a>

# Структуры данных. Стек

-   **LIFO:** Last In First Out

![img](/home/pimiento/yap/Lifo_stack.png)  


<a id="orgbb8e2c3"></a>

# Структуры данных. Граф

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```

![img](/home/pimiento/yap/graph.png)  


<a id="org48c37f7"></a>

# Поиск вглубину. Depth-First Search

```python

def dfs(graph, start, goal):
  stack = [(start, [start])]
  while stack:
    (v, p) = stack.pop()
    paths = set(graph[v]) - set(p)
    for nxt in paths:
      if nxt == goal:
        yield p + [nxt]
      else:
        stack.append((nxt, p+[nxt]))
print(list(dfs(graph, 'A', 'F')))
```

    [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]


<a id="orgcbdf209"></a>

# Глупая сортировка / сортировка дурака

```python
def sort_alg(l):
  while True:
    c = 0
    for i in range(len(l)-1):
      if l[i] > l[i+1]:
        l[i+1],l[i] = l[i],l[i+1]
      else:
        c += 1
    if c == (len(l) - 1): return l

```

```python

print(sort_alg([1, 3, 2, 0]))
```

    [0, 1, 2, 3]


<a id="org766c766"></a>

# Результат глупой сортировки

-   Эффективность **глупой сортировки**: $\mathcal{O}(N^{3})$

>   % ./fool\_sort.py 1K  
> 2 вызовов для 1K данных: лучший результат равен 0.12  
>   % ./fool\_sort.py 2K  
> 2 вызовов для 2K данных: лучший результат равен 0.53  
>   % ./fool\_sort.py 4K  
> 2 вызовов для 4K данных: лучший результат равен 2.15  


<a id="orge7be6d4"></a>

# Пузырьковая сортировка

```python
def sort_alg(l):
  for i in range(len(l)):
    for j in range(len(l[i+1:])):
      if l[j] > l[j+1]:
        l[j], l[j+1] = (l[j+1], l[j])
  return l

print(sort_alg([1, 3, -1, 2, 0]))
```

    [-1, 0, 1, 2, 3]


<a id="org9ea601c"></a>

# Результат пузырьковой сортировки

-   Эффективность **пузырьковой сортировки**: $\mathcal{O}(N^{2})$

>   % ./bubble\_sort.py 1K  
> 2 вызовов для 1K данных: лучший результат равен 0.11  
>   % ./bubble\_sort.py 2K  
> 2 вызовов для 2K данных: лучший результат равен 0.45  
>   % ./bubble\_sort.py 4K  
> 2 вызовов для 4K данных: лучший результат равен 1.86  


<a id="org4500b9a"></a>

# Сортировка слиянием (Merge Sort)

-   <span class="underline"><span class="underline">[Код](https://gist.github.com/pimiento/72ea7cc917e1e732f834e307f6998d89)</span></span>
-   <span class="underline"><span class="underline">[мультик](https://www.youtube.com/watch?v=JSceec-wEyw)</span></span>

Сортировка слиянием позволяет нам распараллелить процесс сортировки. Это очень эффективно на больших данных и широко используется в алгоритмах map/reduce.  


<a id="org113bba5"></a>

# Результат Merge Sort

-   Эффективность **Merge Sort**: $\mathcal{O}(NlogN)$

>   % ./merge\_sort.py 1K  
> 2 вызовов для 1K данных: лучший результат равен 0.01  
>   % ./merge\_sort.py 4K  
> 2 вызовов для 4K данных: лучший результат равен 0.03  
>   % ./merge\_sort.py 8K  
> 2 вызовов для 8K данных: лучший результат равен 0.07  
>   % ./merge\_sort.py 32K  
> 2 вызовов для 32K данных: лучший результат равен 0.31  


<a id="org2bdedf9"></a>

# Сравнение алгоритмов сортировки

![img](/home/pimiento/yap/sorting_algorithms.png)  


<a id="org2ae34f2"></a>

# Устойчивость сортировки

```python
records = [
   {"A": "X", "B": 2},
   {"A": "X", "B": 1},
   {"A": "Y", "B": 1},
]
records.sort(key=lambda x: x["A"])
for r in records:
    print(f"{r['A']}, {r['B']}")
```

    X, 2
    X, 1
    Y, 1


<a id="orgbde7591"></a>

# Как изучать алгоритмы

-   <span class="underline"><span class="underline">[Яндекс.Практикум](https://practicum.yandex.ru/algorithms/)</span></span>
-   Coursera (<span class="underline"><span class="underline">[Part I](https://www.coursera.org/learn/algorithms-part1)</span></span>, <span class="underline"><span class="underline">[Part II](https://www.coursera.org/learn/algorithms-part2)</span></span>)
-   Альманах алгоритмов: Т.Кормен, Ч.Лейзерсон, Р.Ривест, К.Штайн «Алгоритмы. Построение и анализ.»
