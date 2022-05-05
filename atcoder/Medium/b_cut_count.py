N = int(input())
S = input()

def get_cut_count(s:str) -> int:
    ans = 0
    for i in range(len(s)):
        ans = max(ans, len(set(s[i:]) & set(s[:i])))
    return ans

print(get_cut_count(S))

