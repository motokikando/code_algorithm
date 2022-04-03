n, m = map(int, input().split())

def get():
    L = []
    R = []
    for i in range(m):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    ans = min(R)-max(L)+1
    if max(L) > min(R):
        ans = 0
        return ans
    return ans
print(get())
