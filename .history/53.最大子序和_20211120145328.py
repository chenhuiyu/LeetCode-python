#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(nums)]
        for i in range(nums):
            dp[i] = max(nums[i], dp[i - 1])


# @lc code=end
