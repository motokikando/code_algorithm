from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] == target:
                ans = i
                break
            elif target < nums[i]:
                nums.insert(i, target)
                ans = i
                break
            elif target > nums[-1]:
                ans = len(nums)
        return ans




if __name__ == '__main__':
    a = [1, 3, 5, 6 , 8, 10 ,12 ]
    t = 7
    s = Solution()
    print(s.searchInsert(a, t))

