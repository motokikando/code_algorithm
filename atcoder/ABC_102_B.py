from typing import List
N = int(input())
l = list(map(int, input().split()))

def Maximum_Difference(n: int, l: List[int]) -> int:
    ans = max(l) - min(l)
    return ans

print(Maximum_Difference(N, l))
