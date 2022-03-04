import math
a,b = map(str, input().split())
ans = int(a+b)

if math.sqrt(ans).is_integer():
    print("Yes")
else:
    print("No")