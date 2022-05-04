from typing import List
n = int(input())
k = int(input())
l = list(map(int, input().split()))

def collect_ball(k:int, l:List[int]) -> int:
    ans = 0
    for i in range(len(l)):
        if l[i] <= (k-l[i]):
            ans += 2*l[i]
        else:
            ans += (k-l[i])*2
    return ans

print(collect_ball(k, l))
