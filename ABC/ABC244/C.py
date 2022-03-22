import sys
import random
from typing import List
n = int(input())
def gen_f():
    flag = True
    def f():
        nonlocal flag
        if flag:
            flag = False
            return True
        else:
            return False
    return f
f = gen_f()
if f:
    l = [i+1 for i in range(2*n+1)]
    ans = random.choice(l)
    l.pop(ans-1)
    print(ans, flush=True)


def takahashi(n, l:List[int]):
    if len(l)==1:
        sys.exit()
    else:
        l.pop(n-1)
        ans = random.choice(l)
        l.pop(ans-1)
        return ans

print(takahashi(n, l),flush=True)