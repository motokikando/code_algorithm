h, w, y, x, d, m = input().split()
s = [list(input()) for i in range(int(h))]
y = int(y)
x = int(x)

if d == 'N':
  if m == 'L':
    x -= 1
  else:
    x += 1
elif d == 'E':
  if m == 'L':
    y -= 1
  else:
    y += 1
elif d == 'S':
  if m == 'L':
    x += 1
  else:
    x -= 1
elif d == 'W':
  if m == 'L':
    y += 1
  else:
    y -= 1
# print(x,y)

if x < 0 or x >= int(w) or y < 0 or y >= int(h) or s[y][x] == '#':
  print('No')
else:
  print('Yes')

    