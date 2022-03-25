
def main():
    n = int(input())
    rem = set(range(1, 2*n+2))

    while True:
        print(rem.pop(), flush=True)
        a = int(input())
        if a == 0:
            break
        rem.discard(a)
main()