from typing import List
N = int(input())
D, X = map(int, input().split())
A = [int(input()) for i in range(N)]


def sum_chocorate_nums(d:int, x:int, a:List[int]) -> int:
    nums = 0
    for i in range(len(a)):
        nums += get_chocorate_num(a[i], d)
    return x + nums

def get_chocorate_num(a:int, d:int) -> int:
    num = 0
    i = 0
    while i*a+1 <= d:
        num += 1
        i += 1
    return num

print(sum_chocorate_nums(D, X, A))


# n,d,x,*a=map(int,open(0).read().split())
# print(a)
# s=[print(range(1,d+1,c)) for c in a]
# print(s)
# print(sum(s)+x)
