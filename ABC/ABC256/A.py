n, x = map(int, input().split())
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = [v*n for v in a]
print("".join(a)[x-1])

