#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None: return None
        left = 0
        right = len(nums) - 1
        while left <= right:
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
            # 如果左边比mid大，右半部分有序，最大值nums[right]，最小值nums[mid]
            else:
                # 如果target在范围内，在右半部分递归
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                # 否则在左半边递归
                else:
                    right = mid - 1
        return -1


# @lc code=end
