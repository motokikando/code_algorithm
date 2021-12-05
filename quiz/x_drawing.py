#範囲内の各マスについて、斜め線が引かれる位置かどうかを判定するのが楽
#左上・右下方向の斜め線（ (A + k, B + k)(A + k, B + k) を黒く塗る操作）
# 左下・右上方向の斜め線（ (A + k, B − k)(A + k, B − k) を黒く塗る操作）

#N, A, B = map(int,input().split())
#P,Q,R,S = map(int, input().split())

#Height Q - P +1
#Wide S - R +1

#PからQ+1の範囲をループ→i
##ans にリストを格納
##ループでR, S+1
##if i-j==A-B or i+1==A+Bの時
##ansにappendで＃を足す
##それ以外は'.'をたす
#printで（*ans, sep="")を出力

N, A, B = map(int,input().split())
P, Q, R, S = map(int,input().split())

H = Q - P+1
W = S - R+1
for i in range(P, Q+1):
  ans = []
  for j in range(R, S+1):
    if i+j == A+B or i-j==A-B:
      ans.append("#")
    else:
      ans.append('.')
  print(*ans, sep="")


