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
                    nums[i], nums[moreLeft - 1] = nums[moreLeft - 1], nums[i]
                    lessRight -= 1
                # 如果小于等于target，发动到小于区域，小于区右边界右移，i跳下一个
                else:
                    nums[i], nums[lessRight + 1] = nums[lessRight + 1], nums[i]
                    lessRight += 1
                    i += 1
            # 把target和大于区最左边的一个数互换
            nums[lessRight], nums[right] = nums[right], nums[lessRight]

    nums = [5, 1, 1, 2, 0, 0]
    left = 0
    right = len(nums) - 1


# @lc code=end
