from typing import List
n, x = map(int, input().split())
a = list(map(int, input().split()))


def maximaize_children_numbers(n:int, candy:int, a:List[int]) -> int:
    a = sorted(a)
    ans = 0
    for i, child_request in enumerate(a):
        if len(a) == i+1:
            if child_request == candy:
                ans += 1
                break
            else:
                break
        elif candy - child_request >= 0:
            ans += 1
        candy -= child_request

    return ans

print(maximaize_children_numbers(n, x, a))

