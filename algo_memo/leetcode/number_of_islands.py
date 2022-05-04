from typing import List

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         g = grid
#         ans = 0
#         for y in range(len(grid)):
#             for x in range(len(grid[y])):
#                 if g[y][x] == '1':
#                     if y == 0 or y == len(grid)-1 == '0':
#                         if x == 0 and g[y][x+1] and g[y+1][x] == '0' or g[x+1][y] and g[x][y-1] == '0': # g[0][0]の時の判定 (左上角)
#                             ans += 1
#                         elif x == len(grid[y])-1 and g[y][x-1] and g[y+1][x] == '0' or g[y-1][x] and g[x-1][y] == '0':#(右上角)
#                             ans += 1
#                         elif g[y][x-1] and g[y][x+1] == '0' or x ==len(grid[y])-1:
#                             ans += 1




#                     if x == 0 or g[y][x-1] == '0':
#                         if x == len(grid[y])-1 or g[y][x+1] == '0':
#                             ans += 1
#         return ans


class Solution:

    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


if __name__ == '__main__':
    s = Solution()
    g = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

    print(s.numIslands(g))

