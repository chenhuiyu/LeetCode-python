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

        for i in range(2, len(nums)):
            # 1.只有nums[i]
            # 2.不要nums[i],dp[i]=dp[i-1]
            # 3.选nums[i],dp[i]=nums[i]+dp[i-2]
            dp[i] = max(nums[i], dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]


# @lc code=end
