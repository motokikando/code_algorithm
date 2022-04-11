#

n = int(input())
S = set()
for i in range(n):
  s = list(map(str, input().split()))
  S.add(s[0])
  S.add(s[1])


print("Yes" if len(S) >= 2*n-1 else "No")

