A, B, C = map(int, input().split())


def choose_integer(a, b, c) -> str:
    for i in range(1,b):
        if (a*i) % b == c:
            return "YES"
    return "NO"

print(choose_integer(A, B, C))
