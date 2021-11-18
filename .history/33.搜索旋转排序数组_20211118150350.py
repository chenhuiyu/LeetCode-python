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

        while left < right:
            mid = (left + right) // 2
            # 如果中点值=target，返回
            if nums[mid] == target:
                return mid


            # 判断L,M,R三个位置的值是否完全相同
            if nums[left] == nums[right] and nums[mid] == nums[right]:
                # 如果L和M还没有遇到，且L和M的值一直相等，L不断右移
                if left<mid and num[left]== nums[mid]
                left += 1
            # L,M,R三个位置的值不再完全相同，跳出循环
            else:
                continue
            # 运行到此处表示,L,M,R不完全相同
            # 如果L位置的数大于M位置的数，右侧有序
            if nums[left] > nums[mid]:
                # 右侧最大值nums[R],最小值nums[M]
                # 如果target在[nums[M],nums[R]]之间，右侧二分
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                # 如果target不在范围内，左侧二分
                else:
                    right = mid - 1
            # 否则，左侧有序
            # 左侧最大值nums[M]，左侧最小值nums[L]
            else:
                # 如果target在[nums[L],nums[M]]之间，左侧二分
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


# @lc code=end
