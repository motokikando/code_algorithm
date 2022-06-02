s = input()
n = len(s)
ans = "NO"
for i in range(8):
    if s[:7-i] + s[n-i:] == "keyence":
        ans = "YES"
print(ans)