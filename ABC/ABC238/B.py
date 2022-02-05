n = int(input())
l= list(map(int , input().split()))
import numpy as np
a = 0
k = []
k.append(0)
for i in range(n):
    if (a+l[i]) >= 360:
        k.insert(0, a + l[i] - 360)
        a = a + l[i] - 360
    elif a <  360:
        k.insert(0,l[i]+a)
        a += l[i]

k.append(360)

k = sorted(k)
k = np.array(k)
k = np.diff(k, n=1)
print(max(k))

