D, N = map(int, input().split())

def favorite_numbers(d:int, n:int) -> int:
    ans = 0
    if D == 0:
        ans = n
        if n ==100:
            ans += 1
    elif D == 1:
        ans = n*100
        if n == 100:
            ans += 100
    elif D == 2:
        ans = n*10000
        if n == 100:
            ans += 10000
    return ans

# D = 2
# N = 100
print(favorite_numbers(D,N))