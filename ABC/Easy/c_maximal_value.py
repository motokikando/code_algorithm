N = int(input())
B = list(map(int, input().split()))

def get_max_value(l) -> int:
    cnt = l[0]+l[-1]
    for i in range(1, len(l)):
        cnt += min(l[i-1], l[i])
    return cnt

print(get_max_value(B))





