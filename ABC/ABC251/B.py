import itertools
n, w = map(int, input().split())
a = list(map(int, input().split()))

s = set()
for i in range(len(a)):
  if a[i] <= w:
    s.add(a[i])


l = list(itertools.combinations(a,2))
for i in range(len(l)):
  if sum(l[i]) <= w:
    s.add(sum(l[i]))

l2 = list(itertools.combinations(a,3))
for i in range(len(l2)):
  if sum(l2[i]) <= w:

    s.add(sum(l2[i]))

print(len(s))


