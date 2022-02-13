N = int(input())
d = {}
def get_second_mountain(n:int, d:dict) -> str:
    for i in range(n):
        a, b = map(str, input().split())
        b = int(b)
        d.setdefault(a, b)
    d2 = sorted(d.items(), key=lambda x:x[1], reverse=True)
    # print(d)
    # print(d2)
    return d2[1][0]

print(get_second_mountain(N,d))
