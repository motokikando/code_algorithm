num = int(input())

def get_list(n):
    if n == 1:
        return [1]
    else:
        return get_list(n-1) + [n] + get_list(n-1)

print(*get_list(num))
