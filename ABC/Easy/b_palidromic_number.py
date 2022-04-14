A ,B = map(int, input().split())


def get_palindromic_number(a:int, b:int) -> int:
    cnt = 0
    for v in range(a,b+1):
        v = str(v)
        if v[0] == v[4] and v[1] == v[3]:
            cnt += 1
    return cnt

print(get_palindromic_number(A, B))



