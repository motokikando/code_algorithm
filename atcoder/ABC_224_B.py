import numpy as np
n = int(input())
l = []
for i in range(n):
  a = list(map(int, input().split()))
  l.append(a)
cities = l

all_diffs = np.expand_dims(cities, axis=1) - np.expand_dims(cities, axis=0)
degree_distance = np.sqrt(np.sum(all_diffs ** 2, axis=-1))
print(degree_distance.max())