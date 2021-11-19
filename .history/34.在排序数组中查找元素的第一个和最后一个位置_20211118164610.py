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
            mid = (left + right) // 2
            # 中点小于target，在右侧二分
            if nums[mid] <= target:
                # 右侧二分
                left = mid + 1
            # 中点大于target：在左侧二分:
            if nums[mid] > target:
                right = mid - 1
            # 中点处等于target
            # 用mid值更新max_right
            if nums[mid] == target:
                max_right = mid
                min_left = mid


# @lc code=end
