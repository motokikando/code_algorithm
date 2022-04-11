S = input()
if S[-1] == "1" and S.count("1") == 1:
    S = S.replace("1", "0")
    print(S)
    exit(0)
s = int(S, 2)
s = bin(s >> 1)
s = str(s)
l = []
for i in range(2, len(s)):
    l.append(s[i])
l.insert(0, '0')
if "1" not in l:
    print(S)
    exit(0)
if S[0] == "0":
    for i in range(len(S)-len(l)):
        l.insert(0, '0')

print("".join(l))