#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def loop(nums, index, ans):
            # 递归终点，收集答案
            if index == len(nums) - 1:
                print(nums)
                ans.append(nums)
            # i位置和i位置之后的每个数逐个交换
            for j in range(index, len(nums)):
                nums[index], nums[j] = nums[j], nums[index]
                loop(nums, index + 1, ans)
                # 恢复现场
                nums[index], nums[j] = nums[j], nums[index]

        ans = []
        loop(nums, 0, ans)


nums = [1, 2, 3]

# @lc code=end
