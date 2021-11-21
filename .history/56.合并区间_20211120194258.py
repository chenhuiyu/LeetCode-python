#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        start, end = None, None
        for interval in sorted_intervals:
            start_i, end_i = interval
            if start is None:
                start = start_i
            if end is None:
                end = end_i
            if end_i > end:
                end = end_i
            if start_i > end_i:
                ans.append([start, end])
                start = start_i
                end = end_i
        return ans


# @lc code=end
