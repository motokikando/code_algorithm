n , m = map(int, input().split())
a  = list(map(int, input().split()))
b  = list(map(int, input().split()))

ans = ""
for i in range(m):
    if b[i] not in a:
        ans = "No"
        print(ans)
        break
    elif b[i] in a:
        a.remove(b[i])
if ans != "No":
    print("Yes")
