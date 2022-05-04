import re
A, B = map(int, input().split())
S = input()

def judage_regulation(param:str, a:int, b:int) -> str:
    p_regrex = re.fullmatch('\d'*a + "-" + '\d'*b, param)
    if p_regrex:
        print(p_regrex)
        return "Yes"
    else:
        return "No"

print(judage_regulation(S, A, B))