s = input()

def get_b(s:str) -> int:
    l =[]
    for i in range(len(s)):
        if i+2 == len(s):
            break
        int_s = int(s[i]+s[i+1]+s[i+2])
        ans = abs(753 - int_s)
        l.append(ans)
    return min(l)

print(get_b(s))