S = input()

def main(s:str):
    n = len(s)*[0]
    cnt = 0
    for i , v in enumerate(s):
        if v == "R":
            cnt += 1
            continue
        else:
            even = cnt//2
            odd = cnt - even
            n[i] += even
            n[i-1] += odd
            cnt = 0
    cnt  = 0
    for i in range(len(n)-1, -1, -1):
        if s[i] == "L":
            cnt +=1
            continue
        else:
            even = cnt // 2
            odd = cnt - even
            n[i+1] += odd
            n[i] += even
            cnt = 0
    print(*n)

main(S)



