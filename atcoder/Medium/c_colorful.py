from operator import ge
from typing import Tuple, List
n = int(input())
a = list(map(int, input().split()))


def get_color_type(l:List[int]) -> Tuple[int, int]:
    s = set()
    cnt = 0
    for v in l:
        type = v//400
        if v >= 3200:
            s.add(10)
            cnt += 1
        else:
            s.add(type)
    if cnt == 0:
        min = len(s)
        max = len(s)
    elif cnt == len(l):
        min = 1
        max = cnt
    else:
        min = len(s) - 1
        max = len(s) + (cnt -1)
    return min, max

print(*get_color_type(a))



