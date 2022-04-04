n, k, q = map(int, input().split())
l = [k]*n

def main() -> None:
    l = [k]*n
    for i in range(q):
        a = int(input())
        l[a-1] += 1
    for value in l:
        if value - q <= 0:
            print("No")
        else:
            print("Yes")
main()
