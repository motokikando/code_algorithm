# 行数
N = int(input().strip())

# 2次元配列
grid = []
for i in range(N):
    array = list(map(int, input().strip().split()))
    grid.append(array)
#girdをタプルにして配列として再度格納
arr = list(map(list, set(map(tuple, grid))))
print(len(arr))