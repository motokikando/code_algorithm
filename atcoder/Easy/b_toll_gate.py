from typing import List
N, M, X = map(int, input().split())
A = list(map(int, input().split()))

def get_min_distance(n:int, m:List[int], x:int) -> int:
    x_cost = len(set([i for i in range(x)]) & set(m))
    n_cost = len(set(m) & set([i for i in range(x, n)]))
    return min(x_cost, n_cost)

print(get_min_distance(N, A, X))