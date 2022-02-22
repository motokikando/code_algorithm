import math

def power_socket(socket:int, num:int) -> int:
    num -= socket
    if num == 0:
        return 1
    ans = math.ceil(num/(socket -1)+1)
    return ans


a,b = map(int, input().split())
print(power_socket(a, b))
