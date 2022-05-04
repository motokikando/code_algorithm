string = input()

def getss(a:str) -> int:
    b = [v for v in a]
    for i in range(len(b)):
        b.pop()
        if len(b) % 2 == 0:
            if b[:len(b)//2] == b[len(b)//2:]:
                return len(b)

print(getss(string))