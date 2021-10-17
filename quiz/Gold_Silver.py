n = int(input())
a = list(map(int, input().split()))
# n = 5
# a = [2, 3, 4, 5, 2]

ans = [0]*n

for i in range(n-1):
    if a[i] > a[i+1]:
        ans[i] ^= 1
        ans[i+1] ^= 1

print(*ans)

def swap(n, a):
    ans = [0]*n
    for i in range(n-1):
        if a[i] > a[i+1]:
            ans[i] ^= 1
            ans[i+1] ^= 1
    print(*ans)

N = 5
A = [2,3,1,4,2]
swap(N,A)


