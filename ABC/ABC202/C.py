#Nの値を出力
#A,B,Cをそれぞれlist(map(int, input().split())
#Aの出現回数を記録したい　Counter(list)でlist内の要素数を{:}で出力
#ans = 0とする
#Cをループで回すx軸
#yの入力は1なのでindexに合わせてy=x-1となる

from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

dic = Counter(A)

ans = 0

for i in range(N):
    try: #例外が発生しなければ実行
        ans += dic[B[C[i]-1]]
    except:
        pass
print(ans)
