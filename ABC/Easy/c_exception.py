from typing import List
num = int(input())
sequence = [int(input()) for i in range(num)]

def get_max(l: List[int]):
    sort_l = sorted(l)
    for item in l:
        if item != sort_l[-1]:
            print(sort_l[-1])
        else:
            print(sort_l[-2])
get_max(sequence)


