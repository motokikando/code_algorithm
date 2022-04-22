a, b, k = map(int, input().split())

cnt = 0
while(b>a):
    a *= k
    cnt +=1
print(cnt)
