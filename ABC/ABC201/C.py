S = input()
"""
方針
1. 確実にif char in s: で確実に文字が含まれているリストを作成
2. リストO、リストXを作っておく
3. for ループでi, char でenumarate(S)を回す
4. もしcharが=="o"ならOにappend str(i)
5. もしcharが=="x"ならXにappend str(i)

1.asn = 0としておく
2. 文字列sの中に含まれていない数字のリストを作成
3. 10000回ループで文字列.zfill(4)で4桁目まで穴埋め
4. もしjudge関数(s)でTrue判定が出たなら
5. ans に+1

judge関数について
1. リストOのループを回す
2. s内にOの要素がなければ Falseを返す
3. Xも同様でs 内にxの要素があればFalseを返す

"""

T = []
F = []

def judge(s):
    for t in T:
        if t not in s:
            return False

    for f in F:
        if f in s:
            return False
    return True


for i, char in enumerate(S):
    if char == "o":
        T.append(str(i))
    elif char == "x":
        F.append(str(i))

ans = 0

for i in range(10000):
    s = str(i).zfill(4)
    if judge(s):
        ans += 1

print(ans)





