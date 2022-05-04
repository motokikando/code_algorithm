
A, B, C, K= map(int, input().split())

def get_a_minus_b(a, b, c, k) -> int:
    m = k%2
    if m == 0:
        return (a-b)*(-1)**m
    elif m==1:
        return (a-b)*(-1)**m

print(get_a_minus_b(A, B, C, K))
