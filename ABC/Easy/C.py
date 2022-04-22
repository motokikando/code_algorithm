import itertools
import math
n, m, k = map(int, input().split())

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)
l = [i+1 for i in range(m)]
cnt = 0
for v in itertools.product(l, repeat = n):
    print(v)
    if sum(v) <= k:
        cnt +=1
    else:
        break

ans = (permutations_count(m, n)-cnt) % 998244353
print(ans)