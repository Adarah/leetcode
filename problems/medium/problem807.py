from typing import List


class Solution:

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        row_maxima = list(map(max, grid))
        col_maxima = list(map(max, zip(*grid)))
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                row_max = row_maxima[x]
                col_max = col_maxima[y]
                ans += min(row_max, col_max) - grid[x][y]
        return ans


s = Solution()
assert s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]) == 35
