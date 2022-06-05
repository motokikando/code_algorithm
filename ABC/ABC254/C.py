#n, k を入力
#a_list()

#a[i]~a[i+k]をswapしたい
#k回for ループ
##temp = i番目からi+k 飛ばしたlistを格納
##tempをsorted
##a_list[i::k] = temp として格納

#1, n番目までループして リストの前後の大小を比較する
#if a_list[i-1] > a_list[i]した場合 ans = "No"
#return "Yes"

N, K = map(int, input().split())
a_list = list(map(int, input().split()))

def get_k_swap(n, k, l) -> str:
    ans = "Yes"
    for i in range(k):
        l[i::k] = sorted(l[i::k])
    for i in range(1, n):
        if l[i-1] > l[i]:
            ans = "No"
    return ans


print(get_k_swap(N,K,a_list))
