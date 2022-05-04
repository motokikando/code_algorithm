#n種類のチーズ　wを重さの上限(g)とする
#格納するリストを作成しておく l = []
##forループでn回lにappendをして２次元配列を作成　append(list(map(int, input().split())))
#リストをsort(reverse=True))
#oisisa = 0とする
#n回forループ
##i番目の要素をa(チーズの美味しさ度合い),b(重さ(ぐらむ))とする　a, b = l[i]
#もし w == 0: ならbreak
#elif 重さの上限(w)　が b以上の時
##oisisaに　+= a*b
## w -= b
#それ以外
##oisisaにa*wで残りの重さで美味しさを出す
#print(oisisa)

n, w = map(int, input().split())
l = []
for i in range(n):
  l.append(list(map(int, input().split())))
l.sort(reverse=True)
# print(l)
oisisa = 0
for i in range(n):
  a, b = l[i]
  # print(a,b)
  if w == 0:
    break
  elif w >= b:
    oisisa += a*b
    w -= b
  else:
    oisisa += a*w
    w = 0
print(oisisa)

