#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#


# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            # 小于区的左边界
            lessRight = left - 1
            # 大于区的右边界
            moreLeft = right


# @lc code=end
