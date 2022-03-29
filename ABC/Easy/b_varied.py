S = input()

def judge(s:str) -> str:
    l = []
    for i in range(len(s)):
        if s[i] not in l:
            l.append(s[i])
        elif s[i] in l:
            return "no"
    return "yes"

print(judge(S))
