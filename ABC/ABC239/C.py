#方針
# x1, y1, x2, y2 = map(int, input().split())

# if abs(x1 - x2) % 2 == 1 and abs(y1 - y2) % 2 == 1 and abs(x1 - x2) <=3 and abs(y1 - y2) <=3:
#     print("Yes")
# elif x1 == y1 == x2 == y2:
#     print("Yes")
# else:
#     print("No")

def dist_sq(a:int, b:int, c:int, d:int) -> int:
    return (a-c)**2 + (b-d)**2

def solve(x1, y1, x2, y2):
    for x in range(x1 -2, x1+3):
        for y in range(y1 -2, y1 +3):
            if dist_sq(x,y, x1,y1) == dist_sq(x,y,x2,y2) == 5:
                return "Yes"

    return "No"

x1, y1, x2, y2 = map(int, input().split())
print(solve(x1, y1, x2, y2))

