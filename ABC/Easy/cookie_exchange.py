A, B, C = map(int, input().split())

def exchange(a, b, c) -> int:
    if a == b == c and a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        return -1
    ans = 0
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        a, b, c  = int(b/2) + int(c/2), int(a/2) + int(c/2), int(b/2) + int(a/2)
        ans += 1
    return ans


print(exchange(A,B,C))