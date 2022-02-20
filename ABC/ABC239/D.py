import math
A, B, C, D =map(int, input().split())

#全パターン試してみて素数にならないものを見つければTakahashi それ以外はAokiって感じでどうすか
def is_prime(num:int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

ans = ""

for i in range(A,B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            ans = "Aoki"
    if ans != "Aoki":
        ans = "Takahashi"
        print(ans)
        break

if ans != "Takahashi":
    print("Aoki")




