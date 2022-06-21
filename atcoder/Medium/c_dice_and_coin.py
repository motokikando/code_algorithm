N, K = map(int,input().split())

def get_p(n, k) -> float:
    ans = 0
    cnt = 0
    i = 1
    for i in range(1,n+1):
        x = i
        while(x < k):
            x *= 2
            cnt += 1
        ans += float((1/n)*(1/2)**cnt)
        cnt = 0
    return ans

print(get_p(N, K))
