from typing import List
n = int(input())
a = list(map(int, input().split()))

def get_winner(n:int, l:List[int]) -> int:
    A = 0
    B = 0
    l = sorted(l, reverse=True)
    for index, item in enumerate(l):
        if (index + 1) % 2 == 1:
            A += item
        elif (index + 1) % 2 == 0:
            B += item
    return A - B

print(get_winner(n, a))

