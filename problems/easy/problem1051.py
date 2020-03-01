from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct = sorted(heights)
        ans = 0
        for i in range(len(correct)):
            if correct[i] != heights[i]:
                ans += 1
        return ans
