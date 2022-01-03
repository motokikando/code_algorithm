
N = int(input())
# N = 999999999
N = str(N)

def digit_sum(n:str) -> str:
    t = 0
    for i in range(len(str(n))):
        t += int(n[i])
    if int(n) % t == 0:
        ans = 'Yes'
    else:
        ans = 'No'
    return ans

print(digit_sum(N))