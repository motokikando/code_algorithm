from typing import List

class Sort:
    def __init__(self, l:List[int]):
        self.l = l

    def bubble_sort(self) -> List[int]:
        len_numbers = len(self.l)
        for i in range(len_numbers):
            for j in range(len_numbers -1 -i):
                if self.l[j] > self.l[j+1]:
                    self.l[j], self.l[j+1] = self.l[j+1], self.l[j]
        return self.l

    def insertion_sort(self, numbers: List[int]) -> List[int]:
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



input = [3, 7, 5, 1, 7, 8, 2, 9]
s = Sort(input)
print(s.bubble_sort())
print(s.insertion_sort(input))
