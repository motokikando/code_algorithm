import numpy as np
def skillup(n:int, m:int, x:int) -> int:
    # grid = [[60, 2, 2, 4], [70, 1, 1, 1], [50, 2, 3, 9]]
    grid = []
    for i in range(n):
        array = list(map(int, input().strip().split()))
        grid.append(array)
    # print(grid)
    total = []
    for j in range(n**2):
        l = []
        for k in range(n):
            if ((j >> k)& 1):
                # print(grid[k])
                l.append(grid[k])
        # print(l)
        if l != []:
            row_sum = np.sum(l, axis=0)
            # print(row_sum)
            # print(row_sum.shape[0])
            if all(row_sum[elem] >= x for elem in range(row_sum.shape[0])):
                total.append(row_sum[0])
    return min(total, default= -1)



if __name__=='__main__':
    N, M, X = map(int, input().split())
    # N = 3
    # M = 3
    # X = 10
    print(skillup(N,M,X))