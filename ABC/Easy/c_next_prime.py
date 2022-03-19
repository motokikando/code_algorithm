ans = int(input())
import math
def judge_prime(n:int) -> bool:
    if n == 2:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.floor(n**0.5+1), 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


def next_prime(x:int):
    if judge_prime(x):
        return x
    x += 1
    return next_prime(x)
print(next_prime(ans))