N, A, B = map(int, input().split())

def get_some_sums(n:int, a:int, b:int) -> int:
    ans = 0
    for v in range(1, n+1):
        l = [int(i) for i in str(v)]
        if v < 10 and a <= v <= b:
            ans += v
        elif a <= sum(l) <= b:
            ans += v
    return ans

print(get_some_sums(N, A, B))