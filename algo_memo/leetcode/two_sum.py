from typing import List
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        output = []
        pivot = 0
        # targetより大きい値を除外
        for i in reversed(range(len(nums))):
            if nums[i] > target:
               nums.pop(i)

        flag = False
        for i in range(len(nums)):
            for j in range(pivot+1, len(nums)):
                if nums[pivot]+nums[j] == target:
                    output.extend([pivot,j])
                    flag = True
                    break
            if flag:
                break
            pivot += 1
        return output
class Solution2:
    def twoSum(self, nums: List[int], target: int):
        output = {}
        for idx, val in enumerate(nums):
            if target - val in output:
                return (output[target-val], idx)
            output[val] = idx


if __name__== '__main__':
    s = Solution()
    a = [2, 7, 11, 15]
    b = 9
    print(s.twoSum(a, b))

