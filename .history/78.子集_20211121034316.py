#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def loop(nums, index, path, ans):
            if index == len(nums):
                ans.append(path.copy())
                return
            # 要nums[index]
            path.append(nums[index])
            loop(nums, index + 1, path, ans)
            # 恢复现场，不要nums[index]
            path.pop()
            loop(nums, index + 1, path, ans)

        ans = []
        loop(nums, 0, [], ans)
        return ans


# @lc code=end
