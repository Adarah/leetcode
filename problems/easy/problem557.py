class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() 
        ans = ""
        for word in words:
            ans = " ".join([ans, word[::-1]])
        return ans[1:]


s = Solution()
assert s.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
