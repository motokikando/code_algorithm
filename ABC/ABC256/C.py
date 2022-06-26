n = int(input())
s = input()
w = list(map(int, input().split()))
c = [ w[i] for i in range(len(s)) if s[i] == "0"]
a = [ w[i] for i in range(len(s)) if s[i] == "1"]
print(a)
print(c)
c_m = max(c)
a_m = max(a)

num_a = len(a)
num_c = len(c)
for v in a:
    if v < c_m:
        num_a -= 1
for v in c:
    if v < a_m:
        num_c -= 1


c = [ w[i] for i in range(len(c)) if s[i] == "0" and w[i] == c_m]
if num_a >= num_c:
    print(len(a) + len(c))
else:
    print(len(a) + len(c))

