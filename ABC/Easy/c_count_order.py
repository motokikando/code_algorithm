from typing import List
import math
import itertools
num = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def get_count_order(n:int, P:List[int],Q:List[int]) -> int:
    ans = 0
    for idx, item in enumerate(itertools.permutations(sorted(P),len(P))):

        if list(item) == P:
            ans += idx+1
        elif list(item) == Q:
            ans -= idx+1
        elif P == Q:
            ans = 0 
    return abs(ans)


print(get_count_order(num, P, Q))
