H, W = map(int, input().split())
G = [list("."+input()+".") for i in range(H)]
G.append(list("."*(W+2)))
G.insert(0,list("."*(W+2)))
def judge_repainting(g, h, w) -> str:
    ans = 'Yes'
    for y in range(1,h):
        for x in range(1,w):
            if g[y][x] == '#':
                if g[y-1][x] == "." and g[y+1][x] == "." and g[y][x+1] == "." and g[y][x-1] == ".":
                    ans = "No"
                    break;
    return ans
print(judge_repainting(G,H,W))