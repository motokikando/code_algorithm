from typing import List
N = int(input())
V = list(map(int, input().split()))

def get_max_level(n:int, v:List[int]) -> float:
    v.sort()
    result = v[0]
    for i in range(1, n):
        result = (result + v[i])/ 2

    return result

print(get_max_level(N, V))