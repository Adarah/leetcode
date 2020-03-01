from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy_proj = sum(1 for row in grid for i in row if i != 0)
        xz_proj = sum(max(row) for row in grid)
        yz_proj = sum(max(col) for col in zip(*grid))
        return xy_proj + xz_proj + yz_proj


s = Solution()
s.projectionArea([[2]]) == 5
s.projectionArea([[1,2],[3,4]]) == 17
s.projectionArea([[1,0],[0,2]]) == 8
s.projectionArea([[1,1,1],[1,0,1],[1,1,1]]) == 14
s.projectionArea([[1,1,1],[1,0,1],[1,1,1]]) == 21
