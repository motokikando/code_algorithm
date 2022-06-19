import collections
import math
N = int(input())
A = list(map(int, input().split()))

def get_banned_ball(a):
    cnt = 0
    a_dict = collections.Counter(a)
    for v in a_dict.values():
        cnt += int(v*(v-1)/2)
    for i in range(len(a)):
        print(cnt - a_dict[a[i]]+1)


get_banned_ball(A)
