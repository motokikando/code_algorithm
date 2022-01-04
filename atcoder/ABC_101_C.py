
N, K = map(int, input().split())
A = input()
# N = 8
# K = 3


i = 0
E = 1
while E < N:
    E  += (K-1)
    i += 1
print(i)