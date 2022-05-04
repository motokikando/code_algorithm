import collections
w = input()

def get_string(s: str) -> str:
    S = [i for i in s]
    ans = collections.Counter(S)
    for v in ans.values():
        if v % 2 == 1:
            return "No"
    return "Yes"

print(get_string(w))

