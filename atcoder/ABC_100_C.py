N = int(input())
a_n = list(map(int, input().split()))
from typing import List
def three_or_two(n:int, a:List[int]) -> int:
    ans = 0
    flag = True
    while flag:
        if all( i % 2 != 0 for i in a):
            flag = False
            break
        for j in range(n):
            if a[j] % 2 == 0:
                a[j] //= 2
                break
            # else:
            #     a[j] *= 3
        ans += 1
    # print(a)
    return ans



# N = 10
# list_n = [2184, 2126, 1721, 1800, 1024, 2528, 3360, 1945, 1280, 1776]
print(three_or_two(N, a_n))


#解答例
N=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(N):
    if a[i]%2==0:
        tmp=a[i]
        while tmp%2==0:
            tmp=tmp//2
            ans+=1
print(ans)