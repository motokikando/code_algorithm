
# H, W= map(int, input().split())
# S = [list(input()) for i in range(H)]
S = [['#', '.', '#'],['#', '#', '#'],['.', '#', '#']]
H , W = 3, 3

for a in S:
    print(*a)


for y in range(H):
    for x in range(W):
        if x == 0 or S[y][x-1]=='#':
            if x == W-1 or S[y][x+1] == '#':
               print(y,x)


