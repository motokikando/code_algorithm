#Python型ヒントを付ける　from typing import List
# bubble_sortを定義, 変数名はnumbers　def <関数名>(<変数名>:<型>) -><戻り値の型>:
#len_numbers にnumberのlengthを格納
#numbersの長さrangeでforループ returnはnumbers
#並び替えが終わった場合に配列の要素を減らしていくためにrange(len_numbers -1 -i)とする
#もしnumbersのインデックスjのリスト要素が隣のj+1よりも大きい時
#インデックスjのリスト要素とインデックスj+1のリスト要素を入れ替える

from typing import List

def bubble_sort(numbers:List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers -1 -i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers

if __name__ == '__main__':
    nums = [2, 5, 1, 8, 3, 4,]
    bubble_sort(nums)
    print(nums)
