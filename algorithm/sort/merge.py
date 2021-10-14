#merge_sortを定義, 変数名はnumbers def <関数名>(<変数名>:<型>) -><戻り値の型> List[int]:
#len(numbers)の長さ <= 1 の時
#numbers を返す
#分割するためにcenterを定義 len(numbers) // 2
#左側を最初からcenterのindexまでをleftとして定義 numbers[:center]
#右側をcenterから最後までをrightとして定義 numbers[center:right]
#関数としてleft right をそれぞれ呼び出し merge_sort(left)
#leftのindexをi rightのindexをj 並び替えのindexをkとして初期値を0として格納 i=j=k=0
#i と j がそれぞれlen(left) len(right)の長さになるまでwhileでループ:
#もしleftの要素がrightの要素より小さい場合
#numbers[k]に left[i]を代入
#i+1
#else: numbers[k]にrightの要素jを代入
#j+1
#k += 1　while処理の最後に行う
#残りの比べ切れなかった物はwhile文lで追加をしていく
#while i < len(left):の時
#残りのnumbers[k]にleft[i]を入れる
#i += 1 k += 1をする
#while j < len(right):の時
#j += 1 k += 1 をする
#return numbersでリストを返す

from typing import List

def merge_sort(numbers: List[int]) -> List[int]:
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


if __name__ == '__main__':
    nums = [5, 4, 1, 8, 7, 3, 2, 9 ]
    print(merge_sort(nums))
