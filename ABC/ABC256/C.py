n = int(input())
s = input()
w = list(map(int, input().split()))
from collections import defaultdict

d = defaultdict(int)
print(d)

for i in range(n):
    d[w[i]] += (-1,1)[s[i]=="0"] #w[i]のvalueに対して、0なら-1を追加、それ以外は1を追加
    print(d[w[i]])
print(d)

ans = c = s.count("1")
print(ans)
for k in sorted(d):
    c += d[k]
    print(k)
    print(c)
    ans = max(ans,c)
print(ans)
# ansとcでs内の"1"の個数をカウント
#ソートされたDに対して、 kを追加
#d[k]として要素のvalueを追加
#最小値から順番にループ 子供なら+= 1 大人なら-1 を追加
#途中経過時点でのmaxを(ans, c)で比較
#ans でmax(ans, c)同士を比較
#ans を出力

# c = [ w[i] for i in range(len(s)) if s[i] == "0"]
# a = [ w[i] for i in range(len(s)) if s[i] == "1"]
# print(a)
# print(c)
# c_m = max(c)
# a_m = max(a)

# num_a = len(a)
# num_c = len(c)
# for v in a:
#     if v < c_m:
#         num_a -= 1
# for v in c:
#     if v < a_m:
#         num_c -= 1


# c = [ w[i] for i in range(len(c)) if s[i] == "0" and w[i] == c_m]
# if num_a >= num_c:
#     print(len(a) + len(c))
# else:
#     print(len(a) + len(c))

