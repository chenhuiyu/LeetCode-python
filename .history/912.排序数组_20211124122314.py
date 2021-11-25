#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#


# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            L = left - 1
            R = right
            target = nums[right]
            i = left
            while i < right:
                if nums[i] == target:
                    i += 1
                elif nums[i] <= target:
                    nums[i], nums[R] = nums[R], nums[i]
                    R -= 1
                else:
                    nums[i], nums[L] = nums[L], nums[i]
                    L += 1
                    i += 1
            nums[right], nums[R] = nums[R], nums[right]


# @lc code=end
