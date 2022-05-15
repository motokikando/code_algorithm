n = int(input())
l = []
d = {}
for i in range(n):
    a = input().split()
    l.append(a[0])
    value = int(a[1])
    if a[0] not in d:
        d[a[0]] = value
d_max = max(d, key=d.get)
print(l.index(d_max)+1)