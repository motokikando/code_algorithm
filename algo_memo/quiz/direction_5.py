h, w, y, x, n = map(int, input().split())
s = [list(input()) for i in range(h)]
directions = ['N', 'E', 'S', 'W']
now_direction = 0
s[y][x] = '*'

for i in range(n):
  lr, k = input().split()
  k = int(k)
  if lr == 'L':
    now_direction = (3+ now_direction)%4
  else:
    now_direction = (1+now_direction)%4
  flag = False

  for i in range(k):
    if directions[now_direction] == 'N':
      y -= 1
    elif directions[now_direction] == 'S':
      y += 1
    elif directions[now_direction] == 'E':
      x += 1
    elif directions[now_direction] == 'W':
      x -= 1

    if x < 0 or x >= int(w) or y < 0 or y >= int(h) or s[y][x] == '#':
      flag = True
      break
    else:
      s[y][x] = '*'
  # print(y,x)

  if flag:
    # print('Stop')
    break
for a in s:
  print(*a, sep='')




