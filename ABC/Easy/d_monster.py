h = int(input())

def count_attack(h:int) -> int:
    i = 1
    ans = 1
    while h > 1:
        ans += i*2
        h = h//2
        i = i*2
    return ans

print(count_attack(h))