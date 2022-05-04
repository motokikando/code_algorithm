a = input()

def change_bits(bits:str) -> int:
    cnt1 = 0
    cnt2 = 0
    for idx, v in enumerate(bits):
        if idx % 2 == 0 and v != '0':
            cnt1 += 1
        elif idx % 2 == 1 and v != '1':
            cnt1 += 1

    for idx, v in enumerate(bits):
        if idx % 2 == 0 and v != '1':
            cnt2 += 1
        elif idx % 2 == 1 and v != '0':
            cnt2 += 1
    return min(cnt1, cnt2)

print(change_bits(a))
