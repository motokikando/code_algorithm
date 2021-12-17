from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #ListNodeを呼び出す
        dummy = ListNode()
        tail = dummy
		while list1 and list2:
			if list1.val <= list2.val:
				tail.next = list1
				list1 = list1.next
			else:
				tail.next = list2
				list2 = list2.next
			tail = tail.next
		if list1:
			tail.next = list1
		elif list2:
			tail.next = list2
		return dummy.next

if __name__== '__main__':
    s = Solution()
    a = [1, 2, 4]
    b = [1, 3, 4]

    print(s.mergeTwoLists(,))
