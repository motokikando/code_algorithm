

s = set()
#排他的論理和を使う
for i in range(int(input())):
    s ^= {input()}
print(len(s))