#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#


# @lc code=start
class Solution:
    def get_index(self, char):
        if char.isupper():
            char_index = ord(char.lower()) - ord("a") + 26
        else:
            char_index = ord(char) - ord("a")
        return char_index

    def minWindow(self, s: str, t: str) -> str:
        # 如果t比s长，直接返回空串
        if len(s) < len(t):
            return ""

        # 建立一个26*2的英文字母对应表，表示每个字母的欠债情况
        debit = [0 for i in range(26 * 2)]

        length = []

        # 根据被匹配字符t，初始化debit的欠债情况
        for char in t:
            char_index = self.get_char_index(char)
            debit[char_index] -= 1
        # 总欠债情况
        count = len(t)

        # 使用双指针，left、right均初始化在0位置
        left = 0
        right = 0
        # right指针逐渐右扩，并且根据s中的值更新欠债表。
        while right < len(s):
            char = s[right]
            char_index = self.get_char_index(char)
            # 如果s中出现的字母是欠债字符，有效还款，count自减一
            if debit[char_index] < 0:
                count -= 1
            # 更新欠债表
            debit[char_index] += 1

            # 如果所有欠债字符都已经还清，left逐渐右移，缩小整个子串的长度
            if count == 0:
                char = s[left]
                char_index = self.get_char_index(char)
                # 去掉了left处的字符，更新欠债表
                left[char_index] -= 1
                # 如果去掉的是欠债字符，count自增1
                if left[char_index] < 0:
                    count += 1
                left += 1

                if count > 0:
                    length.append([left - 1, right])
        length = sorted(length, key=lambda x: x[1] - x[0], reverse=True)
        min_left, min_right = length[0]
        return s[min_left:min_right]


# @lc code=end


def get_index(char):
    if char.isupper():
        char_index = ord(char.lower()) - ord("a") + 26
    else:
        char_index = ord(char) - ord("a")
    return char_index


def minWindow(s: str, t: str) -> str:
    # 如果t比s长，直接返回空串
    if len(s) < len(t):
        return ""

    # 建立一个26*2的英文字母对应表，表示每个字母的欠债情况
    debit = [0 for i in range(26 * 2)]

    length = []

    # 根据被匹配字符t，初始化debit的欠债情况
    for char in t:
        char_index = get_index(char)
        debit[char_index] -= 1
    # 总欠债情况
    count = len(t)

    # 使用双指针，left、right均初始化在0位置
    left = 0
    right = 0
    # right指针逐渐右扩，并且根据s中的值更新欠债表。
    while right < len(s):
        char = s[right]
        char_index = get_index(char)
        # 如果s中出现的字母是欠债字符，有效还款，count自减一
        if debit[char_index] < 0:
            count -= 1
        # 更新欠债表
        debit[char_index] += 1
        right += 1

        # 如果所有欠债字符都已经还清，left逐渐右移，缩小整个子串的长度
        if count == 0:
            char = s[left]
            char_index = get_index(char)
            # 去掉了left处的字符，更新欠债表
            debit[char_index] -= 1
            # 如果去掉的是欠债字符，count自增1
            if debit[char_index] < 0:
                count += 1
            left += 1

            if count > 0:
                length.append([left - 1, right])
    length = sorted(length, key=lambda x: x[1] - x[0], reverse=True)
    min_left, min_right = length[0]
    return s[min_left:min_right]