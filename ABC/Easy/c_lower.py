from typing import List
num = int(input())
height = list(map(int, input().split()))

def get_lower_height_count(n:int, h:List[int]) -> int:
    cnt = 0
    ans = []
    for i in range(n):
        if i == len(h)-1:
            ans.append(cnt)
            break
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 0
    return max(ans)

print(get_lower_height_count(num, height))