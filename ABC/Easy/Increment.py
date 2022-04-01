num = int(input())
s = input()
def get_max(s:str) -> int:
    cnt = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == "I":
            cnt += 1
        elif s[i] == "D":
            cnt -= 1
        ans = max(cnt, ans)
    return ans

print(get_max(s))
