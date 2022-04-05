from typing import List
num = int(input())
P = list(map(int, input().split()))


def get_low_elements(p:List[int]):
    cnt = 0
    n = 10000000
    for item in p:
        if n > item:
            n = item
            cnt += 1
    return cnt

print(get_low_elements(P))


