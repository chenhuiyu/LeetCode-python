#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 方法1：辅助数组
        max_left = [0 for i in range(len(height))]
        max_right = [0 for i in range(len(height))]


# @lc code=end
