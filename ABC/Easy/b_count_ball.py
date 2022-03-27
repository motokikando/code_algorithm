N, A, B = map(int, input().split())

def count_blue_ball(num, blue:int, red:int) -> int:
    q, mod = divmod(num ,(blue + red))
    if mod <= blue:
        ans = q * blue + mod
    else:
        ans = q * blue + blue
    return ans
print(count_blue_ball(N, A, B))
