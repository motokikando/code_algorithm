s = input()
# s = "aaabd"
n = len(s)
v = []
for k in range(0, n):
  v.append(s[k:n] + s[0:k])
print(min(v))
print(max(v))