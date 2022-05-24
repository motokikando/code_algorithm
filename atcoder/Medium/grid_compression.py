H, W = map(int, input().split())
a = [list(input()) for i in range(H)]

def main(grid):
    grid = [v for v in grid if "#" in v]
    l = []
    for v in zip(*grid):
        if "#" in v:
            l.append(v)
    for v in zip(*l):
        print(*v, sep="")

main(a)



