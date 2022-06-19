import collections
import math
N = int(input())
A = list(map(int, input().split()))

def get_banned_ball(a):
    cnt = 0
    a_dict = collections.Counter(a)
    for b in a:
        a_dict[b] -= 1
        ans = sum([comb(v) for v in a_dict.values() if v >= 2])
        print(ans)
        a_dict[b] += 1
        cnt = 0

def comb(n):
    return math.factorial(n) // (math.factorial(n-2) * math.factorial(2))

get_banned_ball(A)
