#!/usr/bin/env python3
h, w = map(int, input().split())
grid = [["#"] * (w + 2) for _ in range(h + 2)]
for i in range(h):
    s = input()
    for j in range(w):
        grid[i + 1][j + 1] = s[j]

INF = 10 ** 6
dp = [[INF] * (w + 2) for _ in range(h + 2)]
dp[1][1] = int(grid[1][1] == "#")  # 黒なら1、else 0

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if i == 1 and j == 1:
            continue
        val_bottom = dp[i - 1][j] + (grid[i - 1][j] == "." and grid[i][j] == "#")
        print(val_bottom)
        val_left = dp[i][j - 1] + (grid[i][j - 1] == "." and grid[i][j] == "#")
        print(val_left)
        dp[i][j] = min(val_bottom, val_left)
print(dp[h][w])
