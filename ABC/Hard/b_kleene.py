N , K = map(int, input().split())
A = list(map(int, input().split()))

def get_inversion(a, k, n)-> int:
    cnt = 0
    #自分のリスト内の個数
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                cnt += 1
    cnt2 = 0
    #k個の数列から2個選んだ転倒数
    for i in range(n):
        for j in range(n):
            if a[i] > a[j]:
                cnt2 += 1
    ans = cnt*k + cnt2*k*(k-1)//2
    return ans % (10**9+7)

print(get_inversion(A, K, N))




