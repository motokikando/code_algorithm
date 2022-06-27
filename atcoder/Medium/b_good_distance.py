#二次元配列のリストを作成
#nC2回取得を行う
#それぞれの点の距離を求める
import math
import itertools
N, D = map(int, input().split())
A = list(list(map(int, input().split())) for i in range(N))

def get_int_distance(a, d):
    cnt = 0
    for v in itertools.combinations(a, 2):
        sum = 0
        for j in range(d):
            sum += (v[0][j]- v[1][j])**2
        if math.sqrt(sum) % 1 == 0:
            cnt += 1
    return cnt

print(get_int_distance(A, D))
