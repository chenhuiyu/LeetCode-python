#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#


# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            # 划分值
            pivot = nums[right]
            # 小于等于区的右边界
            lessRight = left - 1
            # 大于区的左边界
            moreLeft = right
            # 遍历
            i = left
            while i < moreLeft:
                # 如果比pivot大，放到大于区，大于区左移
                if nums[i] > pivot:
                    nums[i], nums[moreLeft - 1] = nums[moreLeft - 1], nums[i]
                    moreLeft -= 1
                # 如果比pivot小，发送到小于区，小于区右移，指针跳下一个
                elif nums[i] <= pivot:
                    nums[i], nums[lessRight+1] = nums[lessRight+1, nums[i]


# @lc code=end
