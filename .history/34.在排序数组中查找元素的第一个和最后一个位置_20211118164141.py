#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        min_left = len(nums) - 1
        max_right = 0
        while left < right:
            mid=(left + right)//2
            if nums[mid]<=nums[mid]:
                


# @lc code=end
