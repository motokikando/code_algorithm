from typing import List
class Solution:
    def insertionSortList(self, head:List[int]) -> List[int]:
        for i in range(1, len(head)):
            temp = head[i]
            # print(temp)
            j = i-1
            while j >= 0 and head[j] > temp:
                head[j+1] = head[j]
                j -= 1
            head[j+1] = temp
        return head


if __name__ == '__main__':
    nums = [4, 2, 1, 3]
    s = Solution()
    print(s.insertionSortList(nums))

