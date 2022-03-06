from typing import List
k, n = map(int, input().split())
a = list(map(int, input().split()))
def get_distance(lake:int, n:int, a:List[int]) -> int:
    max_distance = 0
    a.append(lake+a[0])

    for i in range(n):
        max_distance  = max(max_distance, a[i+1]-a[i])
    return lake - max_distance

print(get_distance(k, n, a))







