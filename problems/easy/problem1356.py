from typing import List
from collections import defaultdict
from bisect import insort


class Solution():
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans = []
        d = defaultdict(list)
        for i in arr:
            num_of_ones = bin(i).count("1")
            insort(d[num_of_ones], i)
        for key, value in sorted(d.items()):
            ans.extend(value)
        return ans


s = Solution()
assert s.sortByBits([0,1,2,3,4,5,6,7,8]) == [0,1,2,4,8,3,5,6,7]
assert s.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]) == [1,2,4,8,16,32,64,128,256,512,1024]
assert s.sortByBits([1111,7644,1107,6978,8742,1,7403,7694,9193,4401,377,8641,5311,624,3554,6631]) == [1,624,1107,4401,8641,8742,377,1111,6978,3554,7694,9193,5311,6631,7403,7644]
