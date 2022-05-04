from typing import List

#左low 右をhighという引数を使ってint(要素番号)を戻り値とするpartitionのfunctionを作成
def partititon(numbers: List[int], low:int, high:int) -> int:
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
def quick_sort(numbers: List[int]) -> List[int]:
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



if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5, 7]
    print(quick_sort(nums))
