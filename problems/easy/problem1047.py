class Solution:
    def removeDuplicates(self, S: str) -> str:
        j = 0
        found_dupes = True
        while found_dupes:
            found_dupes = False
            while j < len(S)-1:
                if S[j] == S[j+1]:
                    S = S[:j] + S[j+2:]
                    j += 1
                    found_dupes = True
                j += 1
            if found_dupes:
                j = 0
        return S


s = Solution()
assert s.removeDuplicates("abbaca") == "ca"
assert s.removeDuplicates("aababaab") == "ba"
assert s.removeDuplicates("aaaaaaaa") == ""

# this barely solves the problem in time, a better solution would be to BUILD
# the answer instead of trimming S, since you only run through the
# array once that way
