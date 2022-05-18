from typing import List
N = int(input())
A = list(map(int, input().split()))


def get_max_cnt(n:int, a:List[int]) -> int:
    ans = [0]*(10**5+3)
    for v in a:
        ans[v] += 1
        ans[v-1] += 1
        ans[v+1] += 1
    return max(ans)

print(get_max_cnt(N, A))

