from typing import List
N = int(input())
A = list(map(int, input().split()))

def get_student_number(n:int, a:List[int]) -> str:
    ans = [0] * n
    for i in range(n):
        ans[a[i]-1] = i+1

    return " ".join(map(str, ans))

print(get_student_number(N, A)) 