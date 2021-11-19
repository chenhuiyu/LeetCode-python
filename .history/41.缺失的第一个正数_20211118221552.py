#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#


# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # left在初始位置（left左侧的值满足位置i放的i+1）
        left = 0
        # right在右越界位置(表示最好预期)
        right = len(nums)
        while left < right:
            # 如果是大于right的数，不需要
            # 如果是小于left的数，不需要
            # 如果存放的数是left,right之间的val，本应被放到val-1的位置，
            # 但是val-1位置的数存放的已经是val，此时left位置的val也不需要
            if nums[left] > right or nums[left] < left or nums[nums[left] - 1] == nums[left]:
                # 移动到垃圾区
                right -= 1
                nums[left], nums[right] = nums[right], nums[left]
            # 如果left位置放的正好是left+1，left自增1
            elif nums[left] == left + 1:
                left += 1
            # 如果不是不需要的数，但也不是left+1，将这个数放到它对应的位置(val-1)
            # 并与val-1位置上的数交换
            else:
                nums[nums[left] - 1], nums[left] = nums[left], nums[nums[left] - 1]
        return right + 1


# @lc code=end
