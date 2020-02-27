from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        strengths = []
        for row_num in range(len(mat)):
            strengths.append((mat[row_num].count(1), row_num))
        for i in sorted(strengths):
            ans.append(i[1])
            if len(ans) == k:
                break
        return ans


s = Solution()
assert s.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], k = 3) == [2,0,3]

assert s.kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2) == [0,2]
