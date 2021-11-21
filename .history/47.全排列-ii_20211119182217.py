#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#


# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def loop(nums, index, ans, repeat):
            # 收集答案
            if index == len(nums) - 1:
                ans.append(nums.copy())

            # i位置和i位置之后的每个数逐个交换
            for j in range(index, len(nums)):
                if j not in hashmap.keys():
                    hashmap[j] = 1


# @lc code=end
