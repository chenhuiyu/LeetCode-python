'''
Date: 2021-11-15 02:50:54
LastEditors: Chenhuiyu
LastEditTime: 2021-11-17 21:48:42
FilePath: \\.leetcode\\test.py
'''


def add(a, b):
    sum = a
    while (b != 0):
        # 无进位相加
        sum = a ^ b
        # 进位
        b = (a & b) << 1
        a = sum
    return sum


if __name__ == "__main__":
    a = random.randint(100)
