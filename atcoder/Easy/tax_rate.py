import math
N = int(input())

x = math.ceil(N/1.08) #ある値を切り上げ

if math.floor(x*1.08) == N: #切り下げして戻す
    print(x)
else:
    print(":(")



