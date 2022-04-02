A = int(input())
B = int(input())
C = int(input())
X = int(input())


def judge(a, b, c , x) -> int:
    cnt = 0
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i*500+j*100+k*50 == x:
                    cnt += 1
    return cnt

print(judge(A,B,C,X))
