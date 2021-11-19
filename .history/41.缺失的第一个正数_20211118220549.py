#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # left在初始位置
        left=0
        # right在右越界位置
        right=len(nums)
        while left==right:
            # 如果是大于R的数，不需要
            if nums[left]>right

# @lc code=end

