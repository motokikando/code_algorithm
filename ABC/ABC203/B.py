#　累積和
def main():
    n,k = map(int, input().split())
    #n回ループする
    #各階の値を足し合わせる
    #次の会のために+100
    ans = 0
    a = 101
    b = 0
    for j in range(k):
        b += j
    for i in range(n):
        ans += k*a+b
        a += 100
    print(ans)

main()
