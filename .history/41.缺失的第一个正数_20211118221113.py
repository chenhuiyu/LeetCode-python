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
        while left == right:
            # 如果是大于right的数，不需要
            # 如果是小于left的数，不需要
            # 如果存放的数是left,right之间的val，本应被放到val-1的位置，
            # 但是val-1位置的数存放的已经是val，此时left位置的val也不需要
            if nums[left] > right or nums[left] < left or nums[left]:
                # 移动到垃圾区
                right -= 1
                nums[left], nums[right] = nums[right], nums[left]


# @lc code=end
