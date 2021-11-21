#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted(str) not in hashmap.keys():
                hashmap[sorted(str)] = []
                hashmap[sorted(str)].append(str)
            else:
                hashmap[sorted(str)].append(str)
        return list(hashmap)


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# @lc code=end
