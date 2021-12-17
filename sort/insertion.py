from typing import List
def insertion_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i-1 #i番目の左隣のindex
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            # print(numbers[j])
            j -= 1
        numbers[j+1] = temp
    return numbers


if __name__== '__main__':
    nums = [5, 4, 1, 8, 7, 3, 2 ,9]
    print(insertion_sort(nums))
