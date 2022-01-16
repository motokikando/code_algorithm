import math

def is_prime2(num:int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_prime3(num:int) -> bool:
    """
    36 = 1 * 36
    36 = 2 * 18
    36 = 3 * 12
    36 = 4 * 9
    36 = 6 * 6 →√nでもOK
    36 = 9 * 4
    36 = 12 * 3
    36 = 18 * 2
    36 = 36 * 1

    """
    if num <= 1:
        return False
    for i in range(2,math.floor(num**0.5)+1):
        if num % i  == 0:
            return False
    return True


# print(is_prime2(5))

def is_prime4(num:int) -> bool:
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    for i in range(3, math.floor(num**0.5)+1,2):
        if num % i == 0:
            return False
    return False
print(is_prime4(2))