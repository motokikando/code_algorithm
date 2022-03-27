from typing import List
N = int(input())
A = list(map(int, input().split()))


def answer(l:List[int], ans = 0):
    for a in l:
        if a % 2 == 1:
            return ans
    l = list(map(lambda n: int(n/2), l))
    return answer(l, ans+1)
print(answer(A))