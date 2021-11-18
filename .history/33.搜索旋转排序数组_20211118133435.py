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

        while left < right:
            mid = (left + right) // 2
            # 如果中点值=target，返回
            if nums[mid] == target:
                return mid
            else:
                # 在L和M相遇之前，L右移,找到L,M,R三个位置的值不完全相同的位置
                while left <= mid:
                    # 判断L,M,R三个位置的值是否完全相同
                    if nums[left] == nums[right] and nums[mid] == nums[right]:
                        # 如果相同,left右移
                        left += 1
                    # L,M,R三个位置的值不再完全相同，跳出循环
                    else:
                        continue
                # 运行到此处表示,L,M,R不完全相同
                # 如果L位置的数大于M位置的数，右侧有序
                # 右侧最大值nums[R],最小值nums[M]
                if target>=nums[mid] and target<=nums[right]:
                    left=mid+1
                    mid=left+
                # 如果target在[nums[M],nums[R]]之间，右侧二分
                # 如果target不在范围内，左侧二分


# @lc code=end
