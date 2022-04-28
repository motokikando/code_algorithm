S = input()

def get(s:str)-> int:
    a = [0]*(len(s)+1)
    for i in range(len(s)):
        if s[i] == "<":
            a[i+1] = a[i]+1
    for i in range(len(s)-1, -1, -1):
        if s[i] == ">":
            #  a[i] > a[i+1] を比較
            a[i] = max(a[i+1]+1, a[i])
    return sum(a)

print(get(S))