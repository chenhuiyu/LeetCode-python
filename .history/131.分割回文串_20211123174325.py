#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self,s):
        # isPalindromeArray[i][j]表示s[i:j+1]是回文子串
        isPalindromeArray=[[0 for j in range(len(s))] for i in range(len(s))]
        # base case 
        # 中间对角线isPalindromeArray[i][i]只包含字符s[i]，是回文子串
        for i in range(len(s)):
            isPalindromeArray[i][i] = 1


    def partition(self, s: str) -> List[List[str]]:
# @lc code=end

