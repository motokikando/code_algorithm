s = input()

def reversible_count(s: str) -> int:
    cnt = 0
    white_cnt = 0
    for i in range(len(s)):
        if s[i] == "W":
            cnt += i - white_cnt
            white_cnt += 1
    return cnt

print(reversible_count(s))




