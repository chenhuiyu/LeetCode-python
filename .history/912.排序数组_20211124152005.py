#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#


# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            # 小于区的右边界
            lessRight = left - 1
            # 大于区的左边界
            moreLeft = right
            target = nums[right]
            i = left
            # 遍历
            while i < moreLeft:
                # 如果大于target,发送大于区域，大于区左边界左移
                if nums[i] > target:
                    nums[i], nums[moreLeft] = nums[moreLeft], nums[i]


# @lc code=end
