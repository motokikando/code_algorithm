#それぞれの明かりを持っている地点とそれ以外の地点の差を格納二乗和で最小値を決める
#その中でmaxを出力
import math
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = [list(map(int, input().split())) for i in range(n)]

l = [ans[x] for x in range(n) if (x+1) in a]
b = [ans[x] for x in range(n) if (x+1) not in a]
d = []
for i in range(len(b)):
   ans = [abs(l[j][0]-b[i][0])**2 + abs(l[j][1]-b[i][1])**2 for j in range(len(l))]
   d.append(math.sqrt(min(ans)))
print('{:.18g}'.format(max(d)))

