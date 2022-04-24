from typing import List
N =int(input())
w_list = [input() for i in range(N)]

def judge_shiritori(w: List[str]) -> str:
    ans = "Yes"
    if len(w) != len(set(w)):
        ans = "No"
        return ans
    for i in range(len(w)-1):
        if w[i][-1] != w[i+1][0]:
            ans = "No"
            return ans
    return ans

print(judge_shiritori(w_list))

