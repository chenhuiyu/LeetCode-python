#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # # 方法1：辅助数组
        # max_left = [0 for i in range(len(height))]
        # max_right = [0 for i in range(len(height))]

        # max_h = 0
        # for i, h_i in enumerate(height):
        #     max_h = max(max_h, h_i)
        #     max_left[i] = max_h

        # max_h = 0
        # for i in range(len(height) - 1, -1, -1):
        #     max_h = max(max_h, height[i])
        #     max_right[i] = max_h

        # sum = 0
        # for i in range(len(height)):
        #     sum += max(0, min(max_left[i], max_right[i]) - height[i])
        # return sum

        # 方法二：双指针
        # 长度小于3不可能存下水
        height = [4, 2, 0, 3, 2, 5]
        if len(height) < 3:
            return 0
        left = 1
        right = len(height) - 2

        left_max = height[0]
        right_max = height[len(height) - 1]
        water = 0
        while left <= right:
            # left_max = max(left_max, height[left])
            # right_max = max(right_max, height[right])
            if left_max < right_max:
                water += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                water += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1

            # else:
            #     water += max(0, left_max - height[left])
            #     water += max(0, right_max - height[right])
            #     left_max = max(left_max, height[left])
            #     right_max = max(right_max, height[right])
            #     left += 1
            #     right -= 1

        return water


# @lc code=end
