#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#


# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            pivot = nums[right]
            lessRight = left - 1
            moreLeft = right
            i = left


# @lc code=end
