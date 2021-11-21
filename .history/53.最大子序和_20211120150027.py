#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = [0 for i in range(len(nums))]
        pre_max = nums[0]
        for i in range(1, len(nums)):
            max_sum = max(nums[i], pre_max + nums[i])
            pre_max = max_sum
        return max_sum


# @lc code=end
