class Solution:
    def fib(self, N: int) -> int:
        if N == 1:
            return 1
        if N == 0:
            return 0
        return self.fib(N-1) + self.fib(N-2)


s = Solution()
assert s.fib(2) == 1
assert s.fib(3) == 2
assert s.fib(4) == 3
