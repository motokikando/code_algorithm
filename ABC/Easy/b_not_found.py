import string
s = input()
l = list(string.ascii_lowercase)
def get_a(s:str):
    ans = None
    for i in range(len(s)):
        if s[i] in l:
            l.remove(s[i])
            if l == []:
                return None 
    return l[0]

print(get_a(s))

