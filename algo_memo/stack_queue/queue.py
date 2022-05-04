from typing import Any
from collections import deque
# class Queue(object):

#     def __init__(self) -> None:
#         self.queue = []

#     def enqueue(self, data:Any) -> None:
#         self.queue.append(data)

#     def dequeue(self) -> Any:
#         if self.queue:
#             return self.queue.pop(0)

#逆順に並び替える関数
def reverse(queue):
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())
    [q.append(d) for d in new_queue] # 

    # return new_queue


if __name__=='__main__':

    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    q.append(5)
    print(q)
    reverse(q) #リストを逆順に並び替え
    print(q)

