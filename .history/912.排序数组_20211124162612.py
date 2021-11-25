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
                    moreLeft -= 1
                # 如果小于等于target，发动到小于区域，小于区右边界右移，i跳下一个
                else:
                    nums[i], nums[lessRight + 1] = nums[lessRight + 1], nums[i]
                    lessRight += 1
                    i += 1
            # 把target和大于区最左边的一个数互换
            nums[moreLeft], nums[right] = nums[right], nums[moreLeft]
            return moreLeft

        def process(nums, left, right):
            if left >= right:
                return nums
            mid = partition(nums, left, right)
            nums = process(nums, left, mid - 1)
            nums = process(nums, mid + 1, right)

        def sortArray(self, nums: List[int]) -> List[int]:
            nums = process(nums, 0, len(nums) - 1)
            return nums


nums = [5, 2, 4, 1, 6, 2]
left = 0
right = len(nums) - 1
left = 0
right = 3
random.randomint(left, right)

# @lc code=end
