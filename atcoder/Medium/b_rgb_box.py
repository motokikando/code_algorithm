# R, G, B, N = map(int, input().split())

# a = [0]*(N+1)
# a[0]= 1
# print(a)
# def get_rgb_count(r,g,b,n) -> int:
#     cnt = 0

#     return cnt

# print(get_rgb_count(R, G, B, N))

r,g,b,n=map(int,input().split())
a=[0]*(n+1)
a[0]=1
# print(a)
for i in (r,g,b):
    # print(i)
    for j in range(n+1-i):
        a[j+i]+=a[j]
        # print(a)
print(a[n])

#aにn+1の配列を作成
#aの0番目は1とする
#r, g, b それぞれでループ
#j はn+1-i の範囲だけループ
#a[j+i]の位置にa[j]を追加