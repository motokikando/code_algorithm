N, T = map(int, input().split())
a = list(map(int, input().split()))

def get_shower_interval(t, b) -> int:
    cnt = b
    for i in range(len(t)-1):
        interval = t[i+1]-t[i]
        if b <= interval:
            cnt += b
        elif b > interval:
            cnt += interval
    return cnt
print(get_shower_interval(a, T))

