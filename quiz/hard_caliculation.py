s , t = map(int, input().split())
s = str(s)
s = s[::-1]
# print(s)
t = str(t)
t = t[::-1]
# print(t)
x = 0
if len(s) <= len(t):
  a = len(s)
else:
  a = len(t)

for i in range(a):
  if (int(s[i]) + int(t[i])) >= 10:
    print('Hard')
    break
  else:
    x += 1
    if x == a:
      print('Easy')




