a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]

def get_bingo_result():
    for y in range(3):
        for x in range(3):
            for k in range(n):
                if a[y][x] == b[k]:
                    a[y][x] = 0
    ans = "No"
    for i in range(3):
        if a[i][0] + a[i][1] + a[i][2] == 0:
            ans = "Yes"
        elif a[0][i] + a[1][i] + a[2][i] == 0:
            ans = "Yes"
    if a[0][0] + a[1][1] + a[2][2] == 0:
        ans = "Yes"
    elif a[2][0] + a[1][1] + a[0][2] == 0:
        ans = "Yes"

    return ans

print(get_bingo_result())



