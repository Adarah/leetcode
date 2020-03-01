from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counter = Counter(chars)
        ans = 0
        for word in words:
            flag = True
            char_counter_copy = char_counter.copy()
            for letter in word:
                if char_counter_copy[letter] > 0:
                    char_counter_copy[letter] -= 1
                else:
                    flag = False
                    break
            if flag:
                ans += len(word)
        return ans


s = Solution()
assert s.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach") == 6
assert s.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr") == 10
