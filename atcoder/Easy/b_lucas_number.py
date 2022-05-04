
num = int(input())

def get_lucas_number(n:int) -> int:
    l = [0]*(n+1)
    l[0] = 2
    l[1] = 1
    for i in range(2, n+1):
        l[i] = l[i-2] + l[i-1]
    return l[n]

print(get_lucas_number(num))


