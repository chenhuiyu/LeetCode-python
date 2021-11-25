#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        hashmap[nums[0]] = 1
        for i in range(1,len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
                pre= hashmap[nums[i-1]] if nums[i-1] in hashmap else 0
                after= hashmap[nums[i+1]] if nums[i-1] in hashmap else 0
                    hashmap[i-1] =
# @lc code=end
