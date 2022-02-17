S = input()

def reverse(s:str) -> str:
    ans = list(reversed(s))
    for i in range(len(ans)):
        if ans[i] == "6":
            ans[i] = "9"
        elif ans[i] == "9":
            ans[i] = "6"
    return "".join(ans)

print(reverse(S))



