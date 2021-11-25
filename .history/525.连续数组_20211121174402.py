#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
# @lc code=end


nums=[0,1,0]
for i in range(len(nums)):
    if nums[i]==0:
        nums[i]=-1
nums[nums==0] =-1