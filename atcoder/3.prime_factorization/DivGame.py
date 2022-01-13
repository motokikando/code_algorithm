from typing import List
import collections
def factorization(n:int) -> List[int]:
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f*f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
n = int(input())

b = factorization(n)
# print(b)
ans = 0
d = collections.Counter(b)
e = list(d.values())

for i in range(len(d.values())):
    if e[i] > 2:
        ans += 1
        t = 2
        while e[i] > t:
            ans += 1
            e[i] -=  t
            t += 1
    else:
        ans += 1

print(ans)





