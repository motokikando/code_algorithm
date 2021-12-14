from typing import List
class Solution:
    def two_Sum(self, nums: List[int], target:int) -> List[int]:
        output = []
        j = 0
        for i in reversed(range(len(nums))):
            if nums[i] > target:
               nums.pop(i)
        for i in range(len(nums)):
            print(nums[j])




        return nums

if __name__== '__main__':
    s = Solution()
    a = [2,7,11,15]
    b = 9
    print(s.two_Sum(a, b))