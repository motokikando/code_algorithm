from typing import List
import math
class Solution:
    def combinationSum(self, candidates: List[int], target:int) -> List[List[int]]:
        ans = []
        #targetが要素に存在するとき
        if target in candidates:
            ans += [[target]]
        #targetが要素の倍数の時
        for i in range(len(candidates)):
            if target % candidates[i] == 0:
                ans.append([candidates[i] for j in range(int(target/candidates[i]))])


        for i in range(1, (target//2)+1):
            set_target = set([i, target-i])
            print(set_target)
            if set_target <= set(candidates):
                ans.append(list(set_target))

            # print(set_target)

        return ans

class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)






if __name__ == '__main__':
    nums = [2, 3, 7]
    t = 7
    s = Solution2()
    print(s.combinationSum(nums, t))