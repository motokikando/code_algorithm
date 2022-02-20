import math
from  decimal import Decimal
x = int(input())
x = Decimal(x)

if x/10 < 0:
    print(math.floor(x/10))
else:
    print(math.floor(x/10))


