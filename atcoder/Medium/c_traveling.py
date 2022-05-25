N = int(input())
a = [list(map(int, input().split())) for i in range(N)]


def get_Yes_or_No(l) -> str:
    ans = "Yes"
    for i in range(len(l)):
        if i == 0 and (l[0][1]+l[0][2]) > l[0][0]:
            ans = "No"
        if i == (len(l)-1):
            break
        d_time = l[i+1][0] - l[i][0]
        d = (abs(l[i+1][1]-l[i][1])) + abs((l[i+1][2]-l[i][2]))
        if (d_time%2 != d%2 or d > d_time):
            ans = "No"
    return ans

print(get_Yes_or_No(a))




