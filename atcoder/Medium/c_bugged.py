n = int(input())
score_list = [int(input()) for i in range(n)]

def get_max_score(s) -> int:
    ans = sum(s)
    s = sorted(s)
    for v in s:
        if ans % 10 != 0:
            return ans
        if v % 10 != 0:
            ans -= v

    return 0

print(get_max_score(score_list))
