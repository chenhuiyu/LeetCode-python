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
        start, end = sorted_intervals[0][0], sorted_intervals[0][1]
        for interval in sorted_intervals:
            start_i, end_i = interval
            if start_i > end:
                ans.append([start, end])
                start = start_i
                end = end_i
            if end_i > end:
                end = end_i
        # 边界条件！添加最后一对
        ans.append([start, end])
        return ans


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# @lc code=end
