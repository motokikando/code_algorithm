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

    def merge_sort(self, numbers: List[int]) -> List[int]:
        if len(numbers) <= 1:
            return numbers
        center = len(numbers) // 2
        left = numbers[:center]
        right = numbers[center:]

        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        while len(left) > i:
            numbers[k]=left[i]
            i += 1
            k += 1
        while len(right) > j:
            numbers[k]=right[j]
            j += 1
            k += 1
        return numbers

    #左low 右をhighという引数を使ってint(要素番号)を戻り値とするpartitionのfunctionを作成
    def partititon(self, numbers: List[int], low:int, high:int) -> int:
        #iはlow-1からスタートする
        i = low -1
        #pivotはnumbers[high]として定義
        pivot = numbers[high]
        #range(low, high)までをforでループ
        for j in range(low, high):
            #jの要素がpivot以下の時
            if numbers[j] <= pivot:
                #i+1とする(lowのindexを右に1つずらす)
                i += 1
                #numbers[i], numbers[j]を交換する
                numbers[i], numbers[j] = numbers[j], numbers[i]
        #最後にpivotの入っていたnumbers[high]とnumbers[i+1]を入れ替える
        numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
        return i+1

    #quick_sortを定義, 変数名はnumbers def <関数名>(<変数名>:<型>) -><戻り値の型>:
    def quick_sort(self, numbers: List[int]) -> List[int]:
        #inner関数を定義
        def _quick_sort(numbers: List[int], low:int, high:int) -> None:
            #inner関数の中でpartition関数を呼び出す
            #もしlowよりもhighが大きい場合partition_indexにindexを格納
            if low < high:
                #pertition関数を呼び出し(lowとhighの間の部分)要素番号
                partition_index = partititon(numbers, low, high)
                #partitionの左側の部分 partition_index-1がhighとなり_quick_sortを実行
                _quick_sort(numbers, low, partition_index-1)
                #partitionの右側の部分 partition_index+1がlowとなり_quick_sortを実行
                _quick_sort(numbers, partition_index +1, high)
        #初期はnumbers,lowは0 highはlen(numbers)-1 として渡す
        _quick_sort(numbers, 0, len(numbers)-1)
        return numbers



input = [3, 7, 5, 1, 7, 8, 2, 9]
s = Sort(input)
print(s.bubble_sort())
print(s.insertion_sort(input))
