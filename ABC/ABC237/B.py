h, w = map(int,input().split())
#マトリックスの挿入
mat = [list(map(int, input().split())) for i in range(h)]


#zip関数の使用 ([1,2,3],[4,5,6]
#リストに*をつけると配列の要素をそれぞれ引数にす
l = list(zip(*mat))

for i in zip(*mat):
    print(*i)


