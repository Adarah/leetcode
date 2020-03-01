from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for idx, size in enumerate(groupSizes):
            d[size].append(idx)

        ans = []
        for key, value in d.items():
            for i in range(0, len(value), key):
                j = i + key
                ans.append(value[i:j])
        return ans


s = Solution()
assert sorted(s.groupThePeople(groupSizes = [3,3,3,3,3,1,3])) == sorted([[5],[0,1,2],[3,4,6]])
