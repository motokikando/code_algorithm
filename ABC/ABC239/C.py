#方針
x1, y1, x2, y2 = map(int, input().split())

if abs(x1 - x2) % 2 == 1 and abs(y1 - y2) % 2 == 1 and abs(x1 - x2) <=3 and abs(y1 - y2) <=3:
    print("Yes")
elif x1 == y1 == x2 == y2:
    print("Yes")
else:
    print("No")
