# N = int(input())
N = 3
def AtCoDeer(N:int) -> int:
    A, B = 1, 1
    for i in range(N):
        a,b = map(int, input().split())
        ma = max(-(-A//a), -(-B//b))
        A *= ma*a
        B *= ma*b
    return A+B

print(AtCoDeer(N))


