#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        last_max = 0
        for i in range(len(nums)):
            max_sum = max(nums[i], last_max + nums[i])
            last_max = max_sum
        return max(dp)


# @lc code=end
