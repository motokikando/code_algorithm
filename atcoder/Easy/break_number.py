
n = int(input())
def get_break_number(n:int) -> int:
    l = [1, 2, 4, 8, 16, 32, 64]
    a = [i+1 for i in range(n)]
    ans = sorted(list(set(l) & set(a)))

    return ans[-1]

print(get_break_number(n))


