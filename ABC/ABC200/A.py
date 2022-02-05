def get_century(n: int) -> int:
    if n % 100 == 0:
        return n // 100
    else:
        return (n // 100)+1

N =int(input())
print(get_century(N))
