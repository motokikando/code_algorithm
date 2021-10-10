#python型ヒント　from typing import List
#selection_sortを定義, 変数名はnumbers def <関数名>(<変数名>:<型>) -><戻り値の型>:
#len_numbersにnumbersをlenとする returnはnumbers
#numbersの長さrangeでforループ returnはnumbers
#ループ内で最も小さい数を格納するためにmin_indexをiと定義　
#i+1, len_numbersの範囲までfor ループ
#もし i番目の要素numbers[min_idx] j番目の要素よりも大きいとき
#インデックスmin_idxをjとする
#i+1, len_numbersの範囲までfor ループが終わった後, numbersのi番目の要素とmin_indexの要素を入れ替える

from typing import List

def selection_sort(numbers:List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_index = i
        for j in range(i+1, len_numbers):
            if numbers[min_index ] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers
    


if __name__ == '__main__':
    nums = [2,1,3,5,4,6 ]
    selection_sort(nums)
    print(nums)



