import sys
from typing import Optional
class MiniHeap(object):

    def __init__(self) -> None:
        self.heap = [-1*sys.maxsize] #リストを格納
        self.currentsize = 0  #現在のindex番号

    #親nodeを調べる関数
    def parent_index(self, index:int) -> int:
        return index//2

    #leftのchile_indexを参照する
    def left_child_index(self, index:int) -> int:
        return index*2

    #rightの child_index番号を参照する
    def right_child_index(self, index:int) -> int:
        return (index*2)+1

    #index1とindex2の値をswap
    def swap(self, index1:int, index2) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    #parent_indexとindexの要素を参照してindexが小さければswap()を発動する関数
    def heapfy_up(self, index:int) -> None:
        while self.parent_index(index) > 0:
            if self.heap[index]  < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def push(self, value) -> None:
        self.heap.append(value)
        self.currentsize += 1
        self.heapfy_up(self.currentsize)
    from typing import Optional

    def min_child_index(self, index:int) -> int:
        if self.right_child_index(index) > self.currentsize:
            return self.left_child_index(index)
        else:
            if self.heap[self.left_child_index(index)] < self.heap[self.right_child_index(index)]:
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)

    def heapfy_down(self, index:int) -> None:
        #left_child_indexの要素番号がself.current_sizeよりも小さくなるまで行う:
        while self.left_child_index(index) <= self.currentsize:
            min_child_index = self.min_child_index(index)
            if self.heap[index] > self.heap[min_child_index]:
                self.swap(index, min_child_index)
            index = min_child_index



    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return
        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.currentsize -= 1
        self.heapfy_down(1)

        return root

if __name__ == '__main__':
    min_heap = MiniHeap()
    min_heap.push(5)
    min_heap.push(6)
    min_heap.push(2)
    min_heap.push(9)
    min_heap.push(13)
    min_heap.push(11)
    min_heap.push(1)
    min_heap.push(2)
    print(min_heap.heap)
    print(min_heap.pop())
    print(min_heap.heap)
 