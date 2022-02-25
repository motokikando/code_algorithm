from operator import mul
n, m, c = map(int, input().split())
b = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    d = list(map(int, input().split()))
    conbined2 = map(mul, b, d)
    if sum(conbined2)+ c > 0:
        ans += 1

print(ans)

