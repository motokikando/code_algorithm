S = input()

def judge_ATCoder(s:str) -> int:
    ACGT = ["A", "C", "G", "T"]
    ans = []
    judge = 0
    for i in range(len(s)):
        if s[i] in ACGT:
            judge += 1
            if len(s) == judge:
                ans.append(len(s))
            elif i+1 == len(s):
                ans.append(judge)
        else:
            ans.append(judge)
            judge = 0
    return max(ans)

print(judge_ATCoder(S))
