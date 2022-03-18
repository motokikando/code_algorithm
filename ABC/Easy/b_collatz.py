S = int(input())

def get_ans(s:int )-> int:
    i = 1
    nums = set()
    while s not in nums:
        nums.add(s)
        i += 1
        if s % 2 == 0:
            s //= 2
        elif s % 2 == 1:
            s = 3*s+1
    return i
print(get_ans(S))

