from typing import List
import statistics
N = int(input())
D = list(map(int, input().split()))


def devide_list(n:int, d:List[int]) -> int:
    d = sorted(d)
    ans = 0
    med = statistics.median(d)
    if med == int:
        return ans
    for i in range(n):
        if d[i] < med < d[i+1]:
            ans = d[i+1]-d[i]
            break
    return ans

print(devide_list(N, D))