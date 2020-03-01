"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
from typing import List
from collections import deque

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        ans = deque()
        for i in range(1, 1001):
            y_low, y_high = 1, z
            while y_low <= y_high:
                y_mid = (y_low + y_high)//2
                if customfunction.f(i, y_mid) == z:
                    ans.append([i, y_mid])
                    break
                elif customfunction.f(i, y_mid) > z:
                    y_low = y_mid
                else:
                    y_high = y_mid
        return list(ans)
