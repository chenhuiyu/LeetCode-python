#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 如果左边比mid小，左半部分有序，最大值nums[mid]，最小值nums[left]
            if nums[left] <= nums[mid]:
                # 如果target在左边的范围内，在左半边二分
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
            # 否则，在右半边递归
            else:
                left = mid + 1


# @lc code=end
