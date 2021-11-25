#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#


# @lc code=start
class Solution:
    def isPalindrome(self, s):
        # isPalindromeArray[i][j]表示s[i:j+1]是回文子串
        isPalindromeArray = [[0 for j in range(len(s))] for i in range(len(s))]
        # base case
        for i in range(len(s)):
            isPalindromeArray[i][i] = 1
        # 中间对角线isPalindromeArray[i][i]只包含字符s[i]，是回文子串
        # isPalindromeArray[i][i+1]，两个字符，如果相当是回文子串，如果不相等则不是回文
        for i in range(len(s) - 1):
            isPalindromeArray[i][i] = 1
            if s[i] == s[i + 1]:
                isPalindromeArray[i][i + 1] = 1
            else:
                isPalindromeArray[i][i + 1] = 0

        # 如果s[L:R]是回文子串，需要满足s[L]==s[R]，并且s[L-1:R-1]是回文子串isPalindromeArray[L-1][R-1]==1
        for i in range(len(s), -1, -1):
            for j in range(i + 1, len(s)):
                print(i, j)
                if s[i] == s[j] and isPalindromeArray[i - 1][j - 1] == 1:
                    isPalindromeArray[i][j] = 1
                else:
                    isPalindromeArray[i][j] = 0
        return isPalindromeArray

    # def partition(self, s: str) -> List[List[str]]:


s = "aabac"

# @lc code=end
