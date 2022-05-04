import math
h, w = map(int,input().split())
a = [list(input()) for i in range(h)]


def get_count(x, y, s) -> int:
    cnt = 0
    dx, dy  = 0, 0
    flag = False
    route = x+y
    if s[dx][dy] == "#":
        cnt += 1
    for i in range(route):
        dx, dy, flag = get_route(dx, dy, s, cnt)
        if flag:
            cnt += 1
        if dx == (x-1) and dy == (y-1):
            break
    return cnt


def get_route(dx, dy, a, count):
    flag = False
    if a[dx+1][dy] == ".":
        x, y = dx+1, dy
        return x, y , False
    elif a[dx][dy+1] == ".":
        x, y = dx, dy+1
        return x, y, False
    elif a[dx][dy+1] == '#' and a[dx+1][dy] == "#":
        if a[dx+1][dy+1] or a[dx+2][dy] == ".":
            x, y = dx+1, dy
            flag = True
            return x, y, flag
        elif a[dx+1][dy+1] or a[dx][dy+2] == ".":
            x, y = dx+1, dy
            flag = True
            return x, y, flag

print(get_count(h,w,a))


