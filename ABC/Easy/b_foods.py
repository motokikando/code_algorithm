N, M = map(int, input().split())
K = [list(map(int, input().split())) for i in range(N)]
[k.pop(0) for k in K]


def count_loved_foods(L, M) ->int:
    ans = [i+1 for i in range(M)]
    for l in L:
        ans = set(ans) & set(l)
    return len(ans)

print(count_loved_foods(K, M))
