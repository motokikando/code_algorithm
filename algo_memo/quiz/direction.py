x, y, n = map(int, input().split())
directions = ["E", "S", "W", "N"]
now_direction = 0
count = 0
max_count = 1
first = True

def move(direction, x, y):
  if direction == "E":
    x += 1
  elif direction == "S":
    y += 1
  elif direction == "W":
    x -= 1
  elif direction == "N":
    y -= 1
  return (x, y)

for i in range(n):
  (x, y) = move(directions[now_direction], x, y)
  count += 1
  if first and  count == max_count:
    first = False
    count = 0
    now_direction = (now_direction+1)%4

  elif count == max_count:
    first = True
    count = 0
    max_count += 1
    now_direction = (1 + now_direction) % 4
print(x, y)