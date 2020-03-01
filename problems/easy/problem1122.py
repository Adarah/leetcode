from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        ans = []
        for num in arr2:
            ans.extend([num]*c[num])
            del c[num]

        for remaining_nums in sorted(c):
            ans.extend([remaining_nums]*c[remaining_nums])
        return ans


s = Solution()
assert s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
