h, w = map(int, input().split())
S = [list(input()) for i in range(h)]

def judge_minesweeper(s, Y, X):
    dx = [1, 1, 1, 0,-1, -1, -1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(Y):
        for j in range(X):
            if s[i][j] == ".":
                cnt = 0
                for k in range(8):
                    y = i + dy[k]
                    x = j + dx[k]
                    if x >= 0 and x < X and y >= 0 and y < Y and s[y][x] == "#":
                        cnt += 1
                s[i][j] = cnt
    for a in s:
        print(*a, sep="")

judge_minesweeper(S, h, w)



