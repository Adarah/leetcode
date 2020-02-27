from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_wrongs = []  # even positions that have a odd number
        odd_wrongs = []  # odd positions that have an even number
        for i in range(len(A)):
            if i % 2 == 0 and A[i] % 2 != 0:
                even_wrongs.append(i)
            elif i % 2 != 0 and A[i] % 2 == 0:
                odd_wrongs.append(i)

        for j in range(len(even_wrongs)):
            A[even_wrongs[j]], A[odd_wrongs[j]] = A[odd_wrongs[j]], A[even_wrongs[j]]

        return A


s = Solution()
print(s.sortArrayByParityII([3, 1, 4, 2]))
