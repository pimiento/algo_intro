- [Зачем нужны алгоритмы?](#orgfa6b957)
  - [Задача](#org287b54b)
- [Зачем нужны алгоритмы?](#orgd328b73)
- [Результат наивной реализации](#orge0644e6)
- [Бинарный поиск](#org82609ba)
- [Быстрый ThreeSum](#org8bdcb53)
- [Рузельтат быстрого ThreeSum](#org832d748)
- [Алгоритмическая сложность](#org9394a40)
- [Нужны ли алгоритмы backend-разработчику?](#orge74ba26)
- [Какие алгоритмы нужнее всего?](#orgac76c45)
  - [Зависит от задачи, области применения](#org770a687)
- [Структуры данных. Очередь](#org84c4354)
- [Структуры данных. Стек](#orgbab0b96)
- [Структуры данных. Граф](#org76c44ba)
- [Поиск вглубину. Depth-First Search](#orga551468)
- [Глупая сортировка / сортировка дурака](#org98b1921)
- [Результат глупой сортировки](#orgf14689b)
- [Пузырьковая сортировка](#org2bb343a)
- [Сортировка вставками](#orgfe38e73)
- [Сортировка вставками](#org1239667)
- [Сортировка Шелла](#org6dd820d)
- [Быстрая сортировка](#orgc59a19c)
- [Сортировка слиянием (Merge Sort)](#org03f43ba)
- [Сравнение алгоритмов сортировки](#org16ac11f)
- [Устойчивость сортировки](#orgfbe8980)
- [Как изучать алгоритмы](#orga96d90c)

n#+LaTeX\_HEADER: \lstset{basicstyle=\scriptsize\ttfamily}  


<a id="orgfa6b957"></a>

# Зачем нужны алгоритмы?


<a id="org287b54b"></a>

## Задача

Подсчитать, какое количество сочетаний по три элементов входного массива даст в сумме 0.  


<a id="orgd328b73"></a>

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


<a id="orge0644e6"></a>

# Результат наивной реализации

>   % python ./first\_try.py 1K  
> 2 вызовов для 1K данных: лучший результат равен 42.02  
>   % python ./first\_try.py 2K  
> 2 вызовов для 2K данных: лучший результат равен 340.84  


<a id="org82609ba"></a>

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


<a id="org8bdcb53"></a>

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


<a id="org832d748"></a>

# Рузельтат быстрого ThreeSum

>   % python fast\_threesum.py 1K  
> 2 вызовов для 1K данных: лучший результат равен 1.64  
>   % python fast\_threesum.py 2K  
> 2 вызовов для 2K данных: лучший результат равен 7.36  
>   % python fast\_threesum.py 4K  
> 2 вызовов для 4K данных: лучший результат равен 31.31  


<a id="org9394a40"></a>

# Алгоритмическая сложность

![img](/home/pimiento/yap/order_of_growth.png)  


<a id="orge74ba26"></a>

# Нужны ли алгоритмы backend-разработчику?

![img](/home/pimiento/yap/algorithms_for_kids.png)  


<a id="orgac76c45"></a>

# Какие алгоритмы нужнее всего?


<a id="org770a687"></a>

## Зависит от задачи, области применения

-   алгоритмы на строках  
    нужны например биоинформатикам, для работы с последовательностями ДНК
-   алгоритмы на деревьях  
    -   компиляторы
    -   машинное обучение
    -   построение маршрутов
    -   парсинг сайтов


<a id="org84c4354"></a>

# Структуры данных. Очередь

-   **FIFO:** First In First Out

![img](/home/pimiento/yap/Fifo_queue.png)  


<a id="orgbab0b96"></a>

# Структуры данных. Стек

-   **LIFO:** Last In First Out

![img](/home/pimiento/yap/Lifo_stack.png)  


<a id="org76c44ba"></a>

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


<a id="orga551468"></a>

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


<a id="org98b1921"></a>

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

print(sort_alg([1, 3, 2, 0]))
```

    [0, 1, 2, 3]

    [0, 1, 2, 3]

-   Эффективность **глупой сортировки**: $\mathcal{O}(n^{3})$


<a id="orgf14689b"></a>

# Результат глупой сортировки

>   % python ./first\_try.py 1K  
> 2 вызовов для 1K данных: лучший результат равен 42.02  
>   % python ./first\_try.py 2K  
> 2 вызовов для 2K данных: лучший результат равен 340.84  


<a id="org2bb343a"></a>

# Пузырьковая сортировка

```python
def sort_alg(l):
    for i in range(len(l)):
        for j in range(len(l[i+1:])):
            if l[j] > l[j+1]:
                l[j], l[j+1] = (
                    l[j+1], l[j]
                )
    return l


print(sort_alg([1, 3, 2, 0]))
```

    [0, 1, 2, 3]

-   Эффективность **пузырьковой сортировки**: $\mathcal{O}(n^{2})$


<a id="orgfe38e73"></a>

# Сортировка вставками

```python
def sort_alg(l):
    for i in range(1, len(l)):
        k = l[i]
        j = i-1
        print(f"i: {i}; k: {k}")
        while j >= 0 and k < l[j]:
            l[j+1] = l[j]
            print(f"l: {l}")
            j -= 1
        l[j+1] = k
        print(f"j: {j}; l: {l}")

d = [12, 11, 13, 5, 6]
```


<a id="org1239667"></a>

# Сортировка вставками

-   Эффективность **сортировки вставками**: $\mathcal{O}(n^{2})$

**Но!** Эта сортировка эффективна если у вас уже частично отсортированные данные, так как пропускается этап перестановки данных.  

-   <span class="underline"><span class="underline">[Дополнительно почитать](https://habr.com/ru/post/415935/)</span></span>


<a id="org6dd820d"></a>

# Сортировка Шелла

-   <span class="underline"><span class="underline">[Код](https://ru.wikibooks.org/wiki/%25D0%259F%25D1%2580%25D0%25B8%25D0%25BC%25D0%25B5%25D1%2580%25D1%258B_%25D1%2580%25D0%25B5%25D0%25B0%25D0%25BB%25D0%25B8%25D0%25B7%25D0%25B0%25D1%2586%25D0%25B8%25D0%25B8_%25D1%2581%25D0%25BE%25D1%2580%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B8_%25D0%25A8%25D0%25B5%25D0%25BB%25D0%25BB%25D0%25B0#Python)</span></span>
-   на практике получается скорость работы быстрее $\mathcal{O}(n^{2})$ но нет математических описаний как выбор последовательности дистанций влияет на алгоритмическую сложность.


<a id="orgc59a19c"></a>

# Быстрая сортировка

```python
def qsort(L):
    if L:
        return (
            qsort(
        [e for e in L[1:] if e < L[0]]
            ) +
            L[0:1] +
            qsort(
        [e for e in L[1:] if e >= L[0]]
            )
        )
    return []

print(qsort([1, 3, 2, 0]))
```

    [0, 1, 2, 3]


<a id="org03f43ba"></a>

# Сортировка слиянием (Merge Sort)

-   <span class="underline"><span class="underline">[Код](https://gist.github.com/pimiento/72ea7cc917e1e732f834e307f6998d89)</span></span>
-   <span class="underline"><span class="underline">[мультик](https://www.youtube.com/watch?v=JSceec-wEyw)</span></span>

Сортировка слиянием позволяет нам распараллелить процесс сортировки. Это очень эффективно на больших данных и широко используется в алгоритмах map/reduce.  


<a id="org16ac11f"></a>

# Сравнение алгоритмов сортировки

![img](/home/pimiento/yap/sorting_algorithms.png)  


<a id="orgfbe8980"></a>

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


<a id="orga96d90c"></a>

# Как изучать алгоритмы

-   <span class="underline"><span class="underline">[Яндекс.Практикум](https://practicum.yandex.ru/algorithms/)</span></span>
-   Coursera (<span class="underline"><span class="underline">[Part I](https://www.coursera.org/learn/algorithms-part1)</span></span>, <span class="underline"><span class="underline">[Part II](https://www.coursera.org/learn/algorithms-part2)</span></span>)
-   Альманах алгоритмов: Т.Кормен, Ч.Лейзерсон, Р.Ривест, К.Штайн «Алгоритмы. Построение и анализ.»
