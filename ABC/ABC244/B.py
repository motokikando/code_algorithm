
n = int(input())
s = input()
x = 0
y = 0
d = ["E","S","W", "N"]
now_d = 0
max_count = 1

def move(direction, x, y):
  if direction == "E":
    x += 1
  elif direction == "S":
    y -= 1
  elif direction == "W":
    x -= 1
  elif direction == "N":
    y += 1
  return (x, y)


for i in range(len(s)):
    if s[i] == "S":
        (x, y) = move(d[now_d], x, y)
    elif s[i] == "R":
        now_d = (now_d+1)%4
print(x,y)
