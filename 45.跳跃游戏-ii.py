#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        # 初始化三个变量
        # step：到达i位置所需要的最少步数
        step = 0
        # cur：在当前step步数下能到达的最右距离
        cur = 0
        # next：在step+1步数下能到达的最右距离
        next = nums[0]

        for i in range(len(nums)):
            if i > cur:
                step += 1
                cur = next
            next = max(next, i + nums[i])
        return step


nums = [2, 3, 1, 1, 4]

# @lc code=end
