N, K = map(int, input().split())

def replace_integer(n:int, k:int) -> int:
    ans = 0
    if n < k:
        b = n % k
        a = abs(b-k)
        ans = min(a,b)
        return ans
    elif n % k == 0:
        ans = 0
    elif n % k != 0:
        n = n % k
        ans = abs(n-k)
    return ans 

print(replace_integer(N, K))