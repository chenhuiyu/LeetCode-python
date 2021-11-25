#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while s[left].isalpha() is False:
                left += 1
                if left > right:
                    return False
            while s[right].isalpha() is False:
                right -= 1
                if left > right:
                    return False
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


# @lc code=end
