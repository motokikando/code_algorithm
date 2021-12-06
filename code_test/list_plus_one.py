"""
[1] => [2] => 2
[2, 3] => [2, 4] => 24
[8, 9] => [9, 0] => 90
[9, 9] => [1, 0, 0] => 100
[1, 2, 3] => [1, 2, 4] => 124
[7, 8, 9] => [7, 9, 0] => 790
[9, 9, 9] => [1, 0, 0, 0] => 1000
[9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000
[0, 0, 0, 9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000

Can not convert to string such as
l = [1, 2, 3]
print(int(''.join([str(i) for i in l])) + 1)
"""

from typing import List

def plus_one(x: List[int]):
    #逆順にリストを並び替える
    x = list(reversed(x))
    # print(x)
    for i in range(len(x)): #1の位から順番の処理を繰り返す
        x[i] += 1
        if x[i] >= 10:
            if x[-1] == 10:
                x[-1] = 0
                x.append(1)
                break
            x[i] = x[i] % 10

        else:
            break
    x = list(reversed(x))
    print(int(''.join([str(i) for i in x])))

if __name__ == '__main__':
    x = [0, 0, 7, 9, 9]
    plus_one(x)



def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)


def list_to_int(numbers: List[int]) -> int:
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10**i)
    return sum_numbers


def list_to_int_plus_one(numbers: List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break
        numbers[i] = 0
        numbers[i-1] += 1
        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return list_to_int(numbers)


if __name__ == '__main__':
    print(list_to_int_plus_one([0, 0, 0, 9, 9, 9, 9, 9, 9]))