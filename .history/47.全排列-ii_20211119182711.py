#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#


# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def loop(nums, index, ans):
            # 收集答案
            if index == len(nums) - 1:
                ans.append(nums.copy())

            hashmap = []
            # i位置和i位置之后的每个数逐个交换
            for j in range(index, len(nums)):
                # 如果位置的数曾经出现在index位置，剪枝
                # 如果没有，index处的值和j位置的值交换
                # 并将j位置的数加入到hashmap
                if j not in hashmap:
                    hashmap.append(nums[j])
                    nums[index], nums[j] = nums[j], nums[index]
                    loop(nums, index + 1, ans)
                    # 恢复现场
                    nums[index], nums[j] = nums[j], nums[index]

        ans = []
        loop(nums, 0, ans)
        return ans


# @lc code=end
