from collections import Counter
from typing import List


class Solution:
    # def commonChars(self, A: List[str]) -> List[str]:
    #     words = [Counter(word) for word in A]
    #     ans = []
    #     for word in words:
    #         for letter in word.keys():
    #             while all(i[letter] > 0 for i in words):
    #                 ans.append(letter)
    #                 for i in words:
    #                     i[letter] -= 1
    #     print(ans)
    #     return ans
 
    # shamelessly stolen, this was just too good to pass up
    def commonChars(self, A: List[str]) -> List[str]:
        ans = Counter(A[0])
        for word in A:
            ans &= Counter(word)
        return list(ans.elements())



s = Solution()
s.commonChars(["bella","label","roller"])
s.commonChars(["cool","lock","cook"])
