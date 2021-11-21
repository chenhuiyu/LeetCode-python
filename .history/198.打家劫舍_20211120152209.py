#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(nums)]
        # base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])


# @lc code=end
