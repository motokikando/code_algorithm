from typing import List
n = int(input())
x = list(map(int, input().split()))

def get_power(n:int, x:List[int]) -> int:
    x = sorted(x)
    ans = 0
    avg = round(sum(x)/n)
    for i in range(n):
        ans += (avg-x[i])**2
    return ans


print(get_power(n,x))


