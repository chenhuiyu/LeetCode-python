#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        # 如果中点值=target，返回
        if nums[mid] == target:
            return mid
        else:
            # 判断L,M,R三个位置的值是否完全相同
            if nums[left] == nums[right] and nums[mid] == nums[right]:
                # 在L和M相遇之前，L右移
                while left <= mid:
                    # 如果相同,left右移
                    left += 1


# @lc code=end
