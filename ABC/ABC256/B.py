n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

a.append(0)

for i in range(len(l)):
   if a[l[i]-1] != n and a[l[i]-1] != a[l[i]]-1:
      a[l[i]-1] += 1

print(*a[:-1])






