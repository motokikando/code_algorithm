N, K = map(int, input().split())
# 整数nとしてinput
def get_two_handred(n:int, k:int) -> int:
    ans = n
    for i in range(k):
        if ans % 200 == 0:
            ans = int(ans)
            ans //= 200
        else:
            ans = str(ans) + "200"
            ans = int(ans)
    return int(ans)

print(get_two_handred(N, K))
